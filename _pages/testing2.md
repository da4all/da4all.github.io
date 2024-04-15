---
layout: page
permalink: /testing2/
title: Testing 2
description: 
nav: false
nav_rank: 8
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Search Page</title>
</head>
<body>
  <h1>Search Page</h1>

  <!-- Search input field -->
  <input type="text" id="searchInput" placeholder="Search...">
  
  <!-- Search button -->
  <button id="searchButton">Search</button>
  
  <!-- Container for displaying search results -->
  <div id="searchResults"></div>

  <script>
    // Function to perform search
    function performSearch() {
      const searchTerm = document.getElementById('searchInput').value.trim().toLowerCase();

      // Clear previous search results
      document.getElementById('searchResults').innerHTML = '';

      // Loop through each card and search its content
      site.cards.forEach(card => {
        const cardContent = card.title.toLowerCase() + ' ' + card.description.toLowerCase();
        if (cardContent.includes(searchTerm)) {
          // Create card element
          const cardElement = document.createElement('div');
          cardElement.classList.add('card');
          cardElement.classList.add(card.inline ? 'hoverable' : '');
          cardElement.style.marginBottom = '20px';

          const innerHTML = `
            <div class="row no-gutters">
              <div class="team">
                <div class="card-body">
                  <a href="${card.url}">
                    <h5 class="card-title">${card.profile.name}</h5>
                  </a>
                  <p class="card-text">
                    <small class="test-muted">
                      ${card.profile.date ? `<i class="fa-solid fa-calendar"></i>&nbsp; Date: ${card.profile.date}<br>` : ''}
                      ${card.profile.author ? `<i class="fa-solid fa-user"></i>&nbsp; Author: ${card.profile.author}<br>` : ''}
                    </small>
                  </p>
                  <a href="${card.url}">
                    <p class="card-text">${card.teaser}</p>
                  </a>
                  <hr class="solid">
                  <p class="card-text">
                    ${card.profile.source ? `<small class="test-muted"><i class="fas fa-link"></i> Source: <a href="${card.profile.source}">${card.profile.source}</a><br></small>` : ''}
                    ${card.profile.license ? `<small class="test-muted group"><i class="fa-solid fa-quote-left"></i>&nbsp; License: ${card.profile.license}</small><br><br>` : ''}
                  </p>
                  <p class="card-text">
                    <small class="test-muted domain"><i class="fa-solid fa-square"></i>&nbsp; Domain: ${card.domain}</small><br>
                    <small class="test-muted topic"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain: ${card.topic}</small><br>
                    <small class="test-muted group"><i class="fa-solid fa-file"></i>&nbsp; Type of Resource: ${card.group}</small><br>
                  </p>
                </div>
              </div>
            </div>
          `;

          cardElement.innerHTML = innerHTML;

          // Append card element to search results
          document.getElementById('searchResults').appendChild(cardElement);
        }
      });
    }

    // Event listener for search button click
    document.getElementById('searchButton').addEventListener('click', performSearch);
  </script>
</body>
</html>
