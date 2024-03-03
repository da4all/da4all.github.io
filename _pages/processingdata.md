---
layout: page
permalink: /processing-data/
title: Processing Data
description: 
nav: false
nav_rank: 8
---

## Overview

“Processing Data” is a crucial literacy domain for helping students learn how to perform various operations on data so that they can extract valuable insights from data in critical and ethical ways.

Processing Data is often understood to be an iterative cycle involving several phrases. For the purposes of this project, we identify 4 key phases: collecting data; organizing and cleaning data; analyzing and drawing insights from data; and storing and preserving data.

The resources offered under this literacy domain push students to ask critical questions about data processing such as:

- What ethical issues do we need to consider when collecting data?
- What are useful strategies for organizing and cleaning data?
- What are different ways we can analyze data to glean useful information?
- How can we store and preserve data to make it sustainable and accessible?

## Explore the Resources for the "Processing Data" Domain Literacy

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="topic-filter">Subdomain:</label>
    <select id="topic-filter">
    <option value="all">All</option>
    <option value="Collecting Data">Collecting Data</option>
    <option value="Organizing and Cleaning Data">Organizing and Cleaning Data</option>
    <option value="Analyzing and Drawing Insights from Data">Analyzing and Drawing Insights from Data</option>
    <option value="Storing and Preserving Data">Storing and Preserving Data</option>
    </select>

    <br>

    <label for="group-filter">Type of Resource:</label>
    <select id="group-filter">
      <option value="all">All</option>
      {% for group in site.data.cards.groups %}
      <option value="{{ group }}">{{ group }}</option>
      {% endfor %}
    </select>
  </div>
</div>

<div id="card-list">
{% assign cards = site.cards | where: "domain", "Processing Data" | sort: "title" %}

{% for card in cards %}
  <p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title">{{ card.profile.name }}</h5></a>
            <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">{{ card.teaser }}</p></a>
            <p class="card-text">
              <div style="height:1px;font-size:1px;">&nbsp;</div>
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
              <small class="test-muted topic">Topic: {{ card.topic }}</small><br>
              <small class="test-muted group">Group: {{ card.group }}</small><br>
            </p>
          </div>
        </div>
      </div>
    </div>
  </p>
{% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const topicFilter = document.getElementById('topic-filter');
  const groupFilter = document.getElementById('group-filter');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const selectedTopic = topicFilter.value;
    const selectedGroup = groupFilter.value;

    cards.forEach(card => {
      const topic = card.querySelector('.topic').textContent.trim().replace('Topic: ', '');
      const group = card.querySelector('.group').textContent.trim().replace('Group: ', '');

      const topicMatch = selectedTopic === 'all' || topic === selectedTopic;
      const groupMatch = selectedGroup === 'all' || group === selectedGroup;

      if (topicMatch && groupMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  topicFilter.addEventListener('change', filterCards);
  groupFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>

