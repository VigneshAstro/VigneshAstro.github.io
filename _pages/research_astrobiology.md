---
layout: page
title: Astrobiology
permalink: /research/astrobiology/
description: Research articles on planetary habitability, atmospheric evolution, and astrobiology.
nav: false
topic: astrobiology
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<a class="research-back-link" href="{{ '/research/' | relative_url }}"><span aria-hidden="true">←</span> All research themes</a>

<div class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/astrobiology.webp' | relative_url }}"
    alt="A potentially habitable ocean world viewed from space"
    loading="eager"
  >
</div>

<p class="research-topic-intro">
  Astrobiology connects the physical evolution of planets to the environments in which life might emerge and persist. My work examines how
  atmospheric composition, stellar radiation, and planetary history shape habitability and the interpretation of possible biosignatures.
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
