---
layout: page
permalink: /search/
title: Search
description: Search Page
nav: true
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
        {% if content contains search_query %}
            <div class="card" style="margin-bottom: 20px;">
                <h5 class="card-title">{{ card.title }}</h5>
                <p class="card-text">{{ content | replace: search_query, "<span style='background-color: yellow;'>#{search_query}</span>" }}</p>
            </div>
        {% endif %}
    {% endfor %}
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const searchInput = document.getElementById('search-input');
        const searchBtn = document.getElementById('search-button');
        const clearSearchBtn = document.getElementById('clear-search');
        const cardList = document.getElementById('card-list');

        searchBtn.addEventListener('click', function() {
            const searchQuery = searchInput.value.trim().toLowerCase();
            filterCards(searchQuery);
        });

        clearSearchBtn.addEventListener('click', function() {
            searchInput.value = '';
            filterCards('');
        });

        function filterCards(query) {
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                const cardContent = card.querySelector('.card-text').textContent.toLowerCase();
                if (cardContent.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    });
</script>
