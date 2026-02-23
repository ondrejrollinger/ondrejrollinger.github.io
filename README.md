# ondrejrollinger.github.io
Personal blog on GitHub Pages

## Security+ dashboard
- Dashboard: `/secplus/`
- Objective data/status source: `_data/secplus701.yml`

## CompTIA objectives PDF
Place the official CompTIA Security+ SY0-701 Exam Objectives PDF at:
`assets/comptia/CompTIA-Security-Plus-SY0-701-Exam-Objectives-v5.0.pdf`
so the objective pages can embed and deep-link to it.
The official objectives PDF is stored locally under `assets/comptia/` — do not rename without updating the mapping.

## Local development
```bash
sudo bundle install
echo -e "url: 'http://localhost:4000'\nbaseurl: ''" > _config_local.yml
bundle exec jekyll serve --config _config.yml,_config_local.yml --livereload
```

`_config_local.yml` is gitignored — recreate it after every fresh clone.

