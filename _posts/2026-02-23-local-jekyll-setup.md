---
layout: post
title: "Local Jekyll Setup for GitHub Pages (Kali Linux)"
date: 2026-02-23
toc: true
tags: [jekyll]
summary: >
  A reproducible local Jekyll dev environment for this GitHub Pages site on Kali Linux:
  webrick dependency, gem path isolation, gitignore configuration, Liquid tag fixes,
  and a config override for local serving.
---

## Why This Post Exists

Running `bundle exec jekyll serve` locally before pushing to `main` catches build errors
and rendering issues without waiting for GitHub Actions to report a failure. This documents
the exact steps needed to reach a clean local build on Kali Linux, including the problems
encountered and why each fix was necessary.

**Environment:** Kali Linux, system Ruby 3.3, Jekyll 4.3, GitHub Actions CI on Ruby 3.1.

---

## Procedure

### 1. Add `webrick` to Gemfile

`webrick` was removed from Ruby stdlib in 3.x but is required by `jekyll serve`.
It is not needed in CI (no `jekyll serve` runs there) but must be present locally.

```
# Gemfile
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "jekyll-theme-hacker", "~> 0.2"
gem "jekyll-sitemap"
gem "jekyll-feed"
gem "jekyll-seo-tag"
gem "webrick"
```

### 2. Install gems

```
sudo bundle install
```

**Why sudo:** Kali's system Ruby installs gems into `/var/lib/gems/`, which is
root-owned. Running without sudo produces a `Bundler::PermissionError` against
that path.

**Cleaner alternative** (avoids sudo permanently — preferred for a fresh setup):

```
echo 'export GEM_HOME="$HOME/.gems"' >> ~/.rc
echo 'export PATH="$HOME/.gems/bin:$PATH"' >> ~/.rc
source ~/.rc
gem install bundler
bundle install
```

### 3. Update `.gitignore`

```
_site/
_config_local.yml
Gemfile.lock
```

`_site/` is build output — CI generates its own copy, committing it causes
conflicts.

`_config_local.yml` is machine-specific and must never be committed.

`Gemfile.lock` is gitignored because `sudo bundle install` on Kali writes
platform-specific entries (e.g. `x86_64-linux`) that can conflict with CI's gem
resolution. CI resolves gem versions fresh on each run.

**Trade-off:** with no committed lockfile, CI could silently pick up a newer gem
version that breaks the build. If that happens, pin the offending gem directly
in `Gemfile` with an exact version constraint:

```ruby
gem "jekyll-feed", "0.17.0"
```

### 4. Create local config override

CI sets `--baseurl` dynamically via the `configure-pages` action. Locally it
must be empty, otherwise asset links and navigation resolve against the
production URL and break in the browser.

Create `_config_local.yml` — must be recreated manually after every fresh clone:

```
echo -e "url: 'http://localhost:4000'\nbaseurl: ''" > _config_local.yml
```

### 5. Serve

```
bundle exec jekyll serve \
  --config _config.yml,_config_local.yml \
  --livereload
```

Site available at `http://localhost:4000`.

**Evidence of success:** After all fixes, `jekyll serve` produces only Sass
deprecation warnings from `jekyll-theme-hacker-0.2.0`. No Liquid warnings, no
layout warnings, no errors.

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | `bundle install` without sudo | `Bundler::PermissionError` | `/var/lib/gems/` is root-owned on Kali |
| 2 | `jekyll serve` without `webrick` | Aborted immediately on Ruby 3.x | `webrick` removed from stdlib in Ruby 3.0 |
| 3 | Liquid `(tag \| slugify)` inside `append: (...)` | Syntax warnings; broken tag URLs | Strict Liquid disallows pipes inside `append` arguments |
| 4 | `jekyll serve` without `_config_local.yml` | Asset links resolved against production URL | CI sets `--baseurl` dynamically; locally it must be empty |

---

## Current State and Next Steps

**Status:** Local environment operational. Site serves cleanly at `http://localhost:4000`
with live reload.

1. **Sass deprecation warnings** — originate inside `jekyll-theme-hacker-0.2.0`, not
   site code. Will not cause a build failure before Dart Sass 3.0. Revisit when the
   theme releases an update.

2. **Ruby version parity** — local is 3.3, CI is pinned to 3.1 in
   `.github/workflows/deploy.yml`. No divergence observed yet. If a local build passes
   but CI fails, gem version incompatibility is the first thing to check.
