---
layout: page
permalink: /testing3/
title: Testing 3
description: 
nav: false
nav_rank: 8
---

<style>
  .card-container {
    position: sticky;
    top: 80px; /* Adjust as needed based on your header height */
    z-index: 1000; /* Ensure it's above other content */
    background-color: white;
    padding: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .card-title {
    margin-bottom: 5px;
  }

  .toggle-button {
    cursor: pointer;
    margin-left: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
  }

  .toggle-button:hover {
    background-color: #0056b3;
  }
</style>

<div class="card-container">
  <h3 class="card-title">{{ card.title }}</h3>
  <button class="toggle-button">Expand</button>
</div>
<div class="card-content" style="display: none;">
  {{ card.content }}
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-button');

    toggleButtons.forEach(button => {
      button.addEventListener('click', function() {
        const cardContent = this.parentElement.nextElementSibling;
        const isCollapsed = cardContent.style.display === 'none';

        if (isCollapsed) {
          cardContent.style.display = 'block';
          this.textContent = 'Collapse';
        } else {
          cardContent.style.display = 'none';
          this.textContent = 'Expand';
        }
      });
    });
  });
</script>
