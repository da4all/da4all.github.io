---
layout: page
permalink: /search/
title: Search
description: Search 6
nav: false
nav_order: 
---

<!-- Search Bar -->
<div id="search-container" style="background-color: #f2f2f2; padding: 10px;">
    <label for="search-input">Search:</label>
    <input type="text" id="search-input" style="width: 300px;" placeholder="Search by word, phrase, or keyword">
    <button id="search-button">Search</button>
    <button id="clear-search">Clear Search</button>
</div>

<!-- Card Results -->
<div id="card-list" style="margin-top: 20px;">
    {% assign cards = site.pages | where: "layout", "page" %}
    {% for card in cards %}
        {% assign content = card.content | strip_html | strip_newlines %}
        <div class="card" style="margin-bottom: 20px; display: none;">
            <h5 class="card-title">{{ card.title }}</h5>
            <p class="card-text">{{ content }}</p>
        </div>
    {% endfor %}
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const searchInput = document.getElementById('search-input');
        const searchBtn = document.getElementById('search-button');
        const clearSearchBtn = document.getElementById('clear-search');
        const cardList = document.getElementById('card-list');
        const allCards = [...document.querySelectorAll('.card')];

        searchBtn.addEventListener('click', function() {
            const searchQuery = searchInput.value.trim().toLowerCase();
            filterCards(searchQuery);
        });

        clearSearchBtn.addEventListener('click', function() {
            searchInput.value = '';
            filterCards('');
        });

        function filterCards(query) {
            allCards.forEach(card => {
                const cardContent = card.textContent.toLowerCase();
                if (cardContent.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    });
</script>
