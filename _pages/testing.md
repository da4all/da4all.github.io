---
layout: page
permalink: /testing/
title: Testing
description: 
nav: false
nav_rank: 8
---

## Testing 17

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="group-filter">Type of Resource:</label>
    <select id="group-filter">
      <option value="all">All</option>
      {% for group in site.data.cards.groups %}
      <option value="{{ group }}">{{ group }}</option>
      {% endfor %}
    </select>

    <br>
    
    <label for="domain-filter">Primary Domain:</label>
    <select id="domain-filter">
      <option value="all">All</option>
      {% for domain in site.data.cards.domains %}
      <option value="{{ domain }}">{{ domain }}</option>
      {% endfor %}
    </select>

    <br>

    <label for="topic-filter">Subdomain:</label>
    <select id="topic-filter">
      <option value="all">All</option>
      {% for subdomain in site.data.cards.subdomains %}
      <option value="{{ subdomain }}">{{ subdomain }}</option>
      {% endfor %}
    </select>
    
  </div>
</div>

<div id="card-list" style="margin-top: 20px;">
  <div id="cards-container">
  {% assign cards = site.cards | sort: "title" %}
  {% for card in cards %}
    <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px;">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title">{{ card.profile.name }}</h5></a>
            <p class="card-text"><small class="test-muted">{% if card.profile.author %}<i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }}{% endif %}</small></p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">{{ card.teaser }}</p></a>
            <p class="card-text"><br>
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small><br>{% endif %}
              <small class="test-muted domain"><i class="fa-solid fa-square"></i>&nbsp; Domain: {{ card.domain }}</small><br>
              <small class="test-muted topic"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain: {{ card.topic }}</small><br>
              <small class="test-muted group"><i class="fa-solid fa-file"></i>&nbsp; Type of Resource: {{ card.group }}</small><br>
            </p>
          </div>
        </div>
      </div>
    </div>
  {% endfor %}
</div>
<div id="pagination" style="margin-top: 20px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainFilter = document.getElementById('domain-filter');
  const topicFilter = document.getElementById('topic-filter');
  const groupFilter = document.getElementById('group-filter');
  const cardsContainer = document.getElementById('cards-container');
  const paginationContainer = document.getElementById('pagination');
  const cardsPerPage = 6; // Adjust the number of cards per page as needed
  let currentPage = 1;

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedTopic = topicFilter.value;
    const selectedGroup = groupFilter.value;

    const filteredCards = Array.from(cardsContainer.querySelectorAll('.card')).filter(card => {
      const domain = card.querySelector('.domain').textContent.trim().replace('Domain: ', '');
      const topic = card.querySelector('.topic').textContent.trim().replace('Subdomain: ', ''); 
      const group = card.querySelector('.group').textContent.trim().replace('Type of Resource: ', ''); 

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const topicMatch = selectedTopic === 'all' || topic === selectedTopic;
      const groupMatch = selectedGroup === 'all' || group === selectedGroup;

      return domainMatch && topicMatch && groupMatch;
    });

    displayCards(filteredCards, 1);
    displayPagination(filteredCards.length);
  }

  function displayCards(cardsArray, page) {
    const startIndex = (page - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;
    const paginatedCards = cardsArray.slice(startIndex, endIndex);

    cardsContainer.innerHTML = ''; // Clear previous cards

    paginatedCards.forEach(card => {
      cardsContainer.appendChild(card.cloneNode(true));
    });
  }

  function displayPagination(totalCards) {
    const totalPages = Math.ceil(totalCards / cardsPerPage);
    paginationContainer.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
      const button = document.createElement('button');
      button.textContent = i;
      button.addEventListener('click', function() {
        currentPage = i;
        displayCards(Array.from(cardsContainer.querySelectorAll('.card')), currentPage);
      });
      paginationContainer.appendChild(button);
    }
  }

  domainFilter.addEventListener('change', filterCards);
  topicFilter.addEventListener('change', filterCards);
  groupFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>
