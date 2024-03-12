---
layout: page
permalink: /toolkit/
title: Toolkit Overview
description: 
nav: false
nav_rank: 8
---

## Overview

Here you can search all of the cards at once.


## Explore the Resources

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    <label for="search-input">Search:</label>
    <input type="text" id="search-input" placeholder="Enter search query">
  </div>
</div>

<div id="card-list">
{% assign cards = site.cards | sort: "title" %}

{% for card in cards %}
  <p>
    <div class="card" data-domain="{{ card.domain }}" data-topic="{{ card.topic }}" data-group="{{ card.group }}">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            <a href="{{ card.url | relative_url }}">
              <h5 class="card-title">{{ card.profile.name }}</h5>
            </a>
            <p class="card-text"><b>Type of Resource:</b> {{ card.profile.group | replace: '<br />', ', ' }} <br></p>
            <a href="{{ card.url | relative_url }}">
              <p class="card-text">{{ card.teaser }}<small><br><br></small></p>
            </a>
            <p class="card-text">
              {% if card.profile.author %}<small class="test-muted"><i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>&nbsp; Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small><br>{% endif %} 
              <small class="test-muted"><i class="fa-solid fa-diagram-predecessor"></i>&nbsp; Domain: {{ card.domain }} &nbsp;;&nbsp; <i class="fa-solid fa-diagram-successor"></i>&nbsp; Subdomain: {{ card.topic }}</small><br>
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
  const domainFilter = document.getElementById('domain-filter');
  const topicFilter = document.getElementById('topic-filter');
  const groupFilter = document.getElementById('group-filter');
  const searchInput = document.getElementById('search-input');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedTopic = topicFilter.value;
    const selectedGroup = groupFilter.value;
    const searchText = searchInput.value.trim().toLowerCase();

    cards.forEach(card => {
      const domain = card.getAttribute('data-domain').toLowerCase();
      const topic = card.getAttribute('data-topic').toLowerCase();
      const group = card.getAttribute('data-group').toLowerCase();

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const topicMatch = selectedTopic === 'all' || topic === selectedTopic;
      const groupMatch = selectedGroup === 'all' || group === selectedGroup;
      const searchMatch = searchText === '' ||
        card.textContent.toLowerCase().includes(searchText);

      if (domainMatch && topicMatch && groupMatch && searchMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', filterCards);
  topicFilter.addEventListener('change', filterCards);
  groupFilter.addEventListener('change', filterCards);
  searchInput.addEventListener('input', filterCards);

  // Initial hiding of all cards
  cards.forEach(card => {
    card.style.display = 'none';
  });

  // Initial filtering when the page loads
  filterCards();
});
</script>
