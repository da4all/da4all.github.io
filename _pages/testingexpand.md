---
layout: page
permalink: /testingexpand/
title: Testing Expandable Cards
description: 
nav: false
nav_rank: 8
---

{% assign domains = site.data.cards.domains %}

{% for domain in domains %}
  <h2>{{ domain }}</h2>
  <div class="card-container">
    {% for card in site.cards %}
      {% if card.domain == domain %}
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">{{ card.title }}</h3>
            <button class="toggle-button">Expand</button>
          </div>
          <div class="card-content">
            <p>{{ card.teaser }}</p>
            <!-- Add more content here if needed -->
          </div>
        </div>
      {% endif %}
    {% endfor %}
  </div>
{% endfor %}

<script>
  const toggleButtons = document.querySelectorAll('.toggle-button');

  toggleButtons.forEach(button => {
    button.addEventListener('click', () => {
      const content = button.nextElementSibling;
      content.classList.toggle('expanded');
      button.textContent = content.classList.contains('expanded') ? 'Collapse' : 'Expand';
    });
  });
</script>

<style>
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .card-content {
    display: none;
  }

  .card-content.expanded {
    display: block;
  }
</style>

