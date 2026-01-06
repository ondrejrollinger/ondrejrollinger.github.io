# frozen_string_literal: true

module Jekyll
  class TagPage < Page
    def initialize(site, base, dir, tag)
      @site = site
      @base = base
      @dir  = dir
      @name = "index.html"

      process(@name)
      read_yaml(File.join(base, "_layouts"), "tag.html")

      data["tag"] = tag
      data["title"] = "Tag: #{tag}"
    end
  end

  class TagGenerator < Generator
    priority :low

    def generate(site)
      return if site.tags.nil? || site.tags.empty?

      site.tags.keys.each do |tag|
        slug = Utils.slugify(tag.to_s, mode: "default")
        site.pages << TagPage.new(site, site.source, File.join("tag", slug), tag)
      end
    end
  end
end
