---
layout: page
permalink: /testing2/
title: Testing
description: 
nav: false
nav_rank: 8
---
## Option 2:
<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="domain-filter">Primary Domain:</label>
    <select id="domain-filter">
      <option value="all">All</option>
      <option value="Understanding Data">Understanding Data</option>
      <option value="Processing Data">Processing Data</option>
      <option value="Persuading with Data">Persuading with Data</option>
    </select>

    <br>

    <label for="topic-filter">Subdomain:</label>
    <select id="topic-filter">
      <option value="all">All</option>
      <option value="Defining Data">Defining Data</option>
      <option value="Critiquing Data">Critiquing Data</option>
      <option value="Acting Ethically with Data">Acting Ethically with Data</option>
      <option value="Linking Data and Justice">Linking Data and Justice</option>
      <option value="Collecting Data">Collecting Data</option>
      <option value="Organizing and Cleaning Data">Organizing and Cleaning Data</option>
      <option value="Analyzing and Drawing Insights from Data">Analyzing and Drawing Insights from Data</option>
      <option value="Storing and Preserving Data">Storing and Preserving Data</option>
      <option value="Appealing with Data">Appealing with Data</option>
      <option value="Visualizing Data">Visualizing Data</option>
      <option value="Mapping Data">Mapping Data</option>
      <option value="Telling Multi-Modal Stories with Data">Telling Multi-Modal Stories with Data</option>
    </select>

    <br>

    <label for="group-filter">Type of Resource:</label>
    <select id="group-filter">
      <option value="all">All</option>
      <option value="Term">Glossary</option>
      <option value="Reading">Reading</option>
      <option value="Assignment">Assignment</option>
      <option value="Activity">Activity</option>
      <option value="Tutorial">Tutorial</option>
      <option value="Teaching Module">Teaching Module</option>
      <option value="Dataset">Dataset</option>
      <option value="Example of Data Advocacy">Examples of Data Advocacy</option>
    </select>
  </div>
</div>

<div id="card-list">
{% assign cards = site.cards | sort: "title" %}

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
              <small class="test-muted domain">Domain: {{ card.domain }}</small><br>
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
  const domainFilter = document.getElementById('domain-filter');
  const topicFilter = document.getElementById('topic-filter');
  const groupFilter = document.getElementById('group-filter');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedTopic = topicFilter.value;
    const selectedGroup = groupFilter.value;

    cards.forEach(card => {
      const domain = card.querySelector('.domain').textContent.trim().replace('Domain: ', '');
      const topics = [card.querySelector('.topic_2').textContent.trim().replace('Topic: ', ''), card.querySelector('.topic_1').textContent.trim().replace('Topic: ', '')];
      const group = card.querySelector('.group').textContent.trim().replace('Group: ', '');

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const topicMatch = selectedTopic === 'all' || topics.includes(selectedTopic);
      const groupMatch = selectedGroup === 'all' || group === selectedGroup;

      if (domainMatch && topicMatch && groupMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', filterCards);
  topicFilter.addEventListener('change', filterCards);
  groupFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>


