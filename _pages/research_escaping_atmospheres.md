---
layout: page
title: Escaping Atmospheres
permalink: /research/escaping-atmospheres/
description: Research articles on atmospheric escape, metastable helium, thermospheres, and extended planetary tails.
nav: false
topic: escaping-atmospheres
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<a class="research-back-link" href="{{ '/research/' | relative_url }}"><span aria-hidden="true">←</span> All research themes</a>

<div class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/escaping-atmospheres.webp' | relative_url }}"
    alt="An exoplanet losing an extended atmosphere as it transits its star"
    loading="eager"
  >
</div>

<p class="research-topic-intro">
  Metastable helium at 1083 nm is a powerful tracer of gas escaping from irradiated planets. I use high-resolution transmission spectroscopy
  and time-resolved observations to study thermospheres, outflows, and leading and trailing structures that can extend far beyond a planet.
</p>

<h2 class="research-archive-heading">Articles &amp; paper notes</h2>

{% assign research_posts = site.posts | where_exp: "post", "post.categories contains page.topic" | sort: "date" | reverse %}
{% if research_posts.size > 0 %}
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
  <div class="research-empty-state">
    <p>Articles and paper notes will appear here, with the newest first.</p>
  </div>
{% endif %}
