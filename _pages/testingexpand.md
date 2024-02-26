---
layout: page
permalink: /testingexpand/
title: Testing Expandable Cards
description: 
nav: false
nav_rank: 8
---

---
layout: page
title: Card List
---

{% assign domains = site.data.cards.domains %}

{% for domain in domains %}
  <h2>{{ domain }}</h2>
  <div class="card-container">
    {% for card in site.cards %}
      {% if card.domain == domain %}
        <div class="card">
          <h3 class="card-title">{{ card.title }}</h3>
          <button class="toggle-button">Expand</button>
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
  .card-content {
    display: none;
  }

  .card-content.expanded {
    display: block;
  }
</style>


  .card-content.expanded {
    display: block;
  }
</style>

