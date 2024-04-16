---
layout: page
permalink: /testing/
title: Testing
description: 
nav: false
nav_rank: 8
---

## Testing 33

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

    <label for="subdomain-filter">Subdomain:</label>
    <select id="subdomain-filter">
      <option value="all">All</option>
      <option value="Defining Data">Defining Data</option>
      <option value="Critiquing Data">Critiquing Data</option>
      <option value="Acting Ethically with Data">Acting Ethically with Data</option>
      <option value="Linking Data and Justice">Linking Data and Justice</option>
    </select>
    
  </div>
</div>

<div id="card-list" style="margin-top: 20px;">
  {% assign cards = site.cards | sort: "title" %}
  {% for card in cards %}
    <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px;" data-domain="{{ card.domain }}" data-subdomain="{{ card.subdomain }}"> <!-- Add data-domain and data-subdomain attributes -->
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title">{{ card.profile.name }}</h5></a>
            <p class="card-text"><small class="test-muted">{% if card.profile.date %}<i class="fa-solid fa-calendar"></i>&nbsp; Date: {{ card.profile.date | replace: '<br />', ', ' }}{% endif %}
              {% if card.profile.source and card.profile.license %}&nbsp;&nbsp;//&nbsp;&nbsp;{% endif %}
              {% if card.profile.author %}<i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }}{% endif %}</small></p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">{{ card.teaser }}</p></a>
            {% if card.profile.source or card.profile.license %}
              <hr class="solid">
            {% endif %}
            <p class="card-text">
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small>
              {% if card.profile.license %}<br><small class="test-muted"><i class="fa-solid fa-quote-left"></i>&nbsp; License: {{ card.profile.license }}</small><br>{% endif %}{% endif %}
            </p>
              <hr class="solid">
            <p class="card-text">
              <small class="test-muted domain"><i class="fa-solid fa-square"></i>&nbsp; Domain: <a href="{{ site.url }}/{{ card.domain | downcase | replace: ' ', '-' }}">{{ card.domain }}</a>
 &nbsp;&nbsp;//&nbsp;&nbsp;</small>
              <small class="test-muted subdomain"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain: {{ card.profile.subdomain }} &nbsp;&nbsp;//&nbsp;&nbsp;</small>
              <small class="test-muted group"><i class="fa-solid fa-file"></i>&nbsp; Type of Resource: {{ card.group }}</small><br>
            </p>
          </div>
        </div>
      </div>
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainFilter = document.getElementById('domain-filter');
  const subdomainFilter = document.getElementById('subdomain-filter');
  const groupFilter = document.getElementById('group-filter');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedSubdomain = subdomainFilter.value;
    const selectedGroup = groupFilter.value;

    cards.forEach(card => {
      const domain = card.getAttribute('data-domain'); // Get domain from data attribute
      const subdomain = card.getAttribute('data-subdomain'); // Get subdomain from data attribute
      const group = card.querySelector('.group').textContent.trim().replace('Type of Resource: ', ''); 

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const subdomainMatch = selectedSubdomain === 'all' || subdomain === selectedSubdomain;
      const groupMatch = selectedGroup === 'all' || group === selectedGroup;

      if (domainMatch && subdomainMatch && groupMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', filterCards);
  subdomainFilter.addEventListener('change', filterCards);
  groupFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>
