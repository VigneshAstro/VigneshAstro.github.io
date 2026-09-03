---
layout: page
title: Temperate Planet Atmospheres
permalink: /research/temperate-planet-atmospheres/
description: Research articles on the atmospheres of small, temperate planets orbiting nearby stars.
nav: false
topic: temperate-planet-atmospheres
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<a class="research-back-link" href="{{ '/research/' | relative_url }}"><span aria-hidden="true">←</span> All research themes</a>

<div class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/temperate-planets.webp' | relative_url }}"
    alt="A small temperate planet transiting a cool red star"
    loading="eager"
  >
</div>

<p class="research-topic-intro">
  Nearby M dwarfs offer some of the best opportunities to study small, cool planets. I investigate what observations can reveal about their
  atmospheres - from constraints on primordial hydrogen and helium to the prospects for characterizing temperate terrestrial worlds.
</p>

<h2 class="research-archive-heading">Current work</h2>

<div class="research-feature-list">
  <article class="research-feature research-feature--status">
    <div class="research-feature__copy">
      <time datetime="2026">Ongoing</time>
      <h3>JWST studies of temperate planetary atmospheres</h3>
      <p>
        New JWST studies are underway. These observations are designed to test what atmospheres small, temperate planets can retain and how
        stellar activity and surface-atmosphere interactions influence the spectra we measure. Stay tuned for interesting results.
      </p>
    </div>
  </article>
</div>

{% assign research_posts = site.posts | where_exp: "post", "post.categories contains page.topic" | sort: "date" | reverse %}
{% if research_posts.size > 0 %}

  <h2 class="research-archive-heading research-archive-heading--secondary">Articles &amp; paper notes</h2>
  <div class="research-article-list">
    {% for post in research_posts %}
      <article class="research-article-card">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        {% if post.description %}<p>{{ post.description }}</p>{% endif %}
        <a class="research-article-card__link" href="{{ post.url | relative_url }}">Read article <span aria-hidden="true">→</span></a>
      </article>
    {% endfor %}
  </div>
{% else %}
{% endif %}
