---
layout: page
permalink: /persuading-with-data/
title: Persuading with Data
description: 
nav: false
nav_rank: 8
---

## Overview

“Persuading with Data” is a crucial literacy domain for helping students learn how to generate persuasive data-driven content to assist advocacy aims for diverse contexts, purposes, and audiences.

Persuading with Data is a multi-modal affair, meaning that when it comes to data advocacy, not only does data often come in various forms (numerical, imagistic, geolocational) but data is also commonly woven together with various resources for communication (words, sounds, images, etc.) to achieve various aims. To help students learn the various multi-modal ways one can persuade with data for advocacy purposes, we offer resources that specifically focus on: appealing with data; visualizing data; mapping data; and telling multi-modal stories with data.

The resources offered under this literacy domain focus on these and other important questions:

- How can rhetoric—the art of persuasion—inform and enhance our data advocacy efforts?
- How can we use data to make emotional, ethical, and logical appeals to help achieve our advocacy aims?
- How can data visualizations and maps be responsibly used to assist our advocacy efforts?
- How can we tell ethical, effective, and affective data-driven stories to achieve our various rhetorical aims?

## Explore the Resources for the "Persuading with Data" Domain Literacy

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="topic-filter">Subdomain:</label>
    <select id="topic-filter">
    <option value="all">All</option>
    <option value="Appealing with Data">Appealing with Data</option>
    <option value="Visualizing Data">Visualizing Data</option>
    <option value="Mapping Data">Mapping Data</option>
    <option value="Telling Multi-Modal Stories with Data">Telling Multi-Modal Stories with Data</option>
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
{% assign cards = site.cards | where: "domain", "Persuading with Data" | sort: "title" %}

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

