---
layout: page
permalink: /understanding-data/
title: Understanding Data
description: 
nav: false
nav_rank: 8
---

## Overview

“Understanding data” is a crucial literacy domain for helping students develop the critical, ethical, and rhetorical impulses needed to define data; understand its complicated relations to power, privilege, oppression, and liberation; and imagine ethical and responsible ways of working with data toward more just futures.

The resources offered under this literacy domain push students to ask critical questions about data such as:
- What is “data”?
- How and why does data ethically matter?
- What critical habits toward data are important to develop?
- What rhetorical dimensions of data need to be considered?
- What is data advocacy? And how can we do data advocacy ethically and responsibly?

## Explore the Resources for "Understanding Data"

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="topic-filter">Subdomain:</label>
    <select id="topic-filter">
    <option value="all">All</option>
    <option value="Defining Data">Defining Data</option>
    <option value="Critiquing Data">Critiquing Data</option>
    <option value="Acting Ethically with Data">Acting Ethically with Data</option>
    <option value="Linking Data and Justice">Linking Data and Justice</option>
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
{% assign cards = site.cards | where: "domain", "Understanding Data" | sort: "title" %}

{% for card in cards %}
  <p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title">{{ card.profile.name }}</h5></a>
            <p class="card-text">{% if card.profile.author %}<small class="test-muted"><i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">{{ card.teaser }}<small><br><br></small></p></a>
            <p class="card-text">
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
              <small class="test-muted topic"><i class="fa-solid fa-diagram-successor"></i>&nbsp; Subdomain: {{ card.topic }}</small><br>
              <small class="test-muted group"><i class="fa-solid fa-file"></i>&nbsp; Type of Resource: {{ card.group }}</small><br>
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

