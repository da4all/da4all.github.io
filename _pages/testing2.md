---
layout: page
permalink: /testing2/
title: Testing 2
description: 
nav: false
nav_rank: 8
---

<!DOCTYPE html>
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
  
  <!-- Container for displaying search results -->
  <div id="searchResults"></div>

  <!-- Pagination container -->
  <div id="pagination"></div>

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
          // Display the card in the search results
          const cardElement = document.createElement('div');
          cardElement.textContent = card.title;
          document.getElementById('searchResults').appendChild(cardElement);
        }
      });

      // Update pagination if needed
      // You can implement pagination logic here if necessary
    }

    // Event listener for search input
    document.getElementById('searchInput').addEventListener('input', performSearch);

    // Initial search to display all cards
    performSearch();
  </script>
</body>
</html>
