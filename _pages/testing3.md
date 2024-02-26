---
layout: page
permalink: /testing3/
title: Testing 3
description: 
nav: false
nav_rank: 8
---

<div id="cards-container">
  {% assign cards = site.cards | sort: "title" %}
  
  {% for domain in site.data.cards.domains %}
    <h2>{{ domain }}</h2>
    <div class="domain-cards">
      {% for card in cards %}
        {% if card.domains contains domain %}
          <div class="card">
            <h3>{{ card.title }}</h3>
            <div class="card-content" style="display: none;">
              {{ card.content }}
            </div>
            <button class="toggle-button">Toggle Content</button>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const toggleButtons = document.querySelectorAll('.toggle-button');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
      const cardContent = this.parentElement.querySelector('.card-content');
      cardContent.style.display = cardContent.style.display === 'none' ? 'block' : 'none';
    });
  });
});
</script>
