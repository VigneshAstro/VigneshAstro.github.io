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
  atmospheres—from constraints on primordial hydrogen and helium to the prospects for characterizing temperate terrestrial worlds.
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
