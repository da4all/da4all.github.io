{% comment %}
Core code for generating filterable lesson indexes on lessons.md and es/lecciones.md. This will repeatedly call
lesson_describe.html in which individual lessons have their metadata formatted for display.
{% endcomment %}
<!-- loading graph if search in URI -->
<div id="pre-loader">
  <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid"
    class="lds-ripple" style="background:0 0">
    <circle cx="50" cy="50" r="4.719" fill="none" stroke="#1d3f72" stroke-width="2">
      <animate attributeName="r" calcMode="spline" values="0;40" keyTimes="0;1" dur="3" keySplines="0 0.2 0.8 1" begin="-1.5s" repeatCount="indefinite" />
      <animate attributeName="opacity" calcMode="spline" values="1;0" keyTimes="0;1" dur="3" keySplines="0.2 0 0.8 1" begin="-1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="50" cy="50" r="27.591" fill="none" stroke="#5699d2" stroke-width="2">
      <animate attributeName="r" calcMode="spline" values="0;40" keyTimes="0;1" dur="3" keySplines="0 0.2 0.8 1" begin="0s" repeatCount="indefinite" />
      <animate attributeName="opacity" calcMode="spline" values="1;0" keyTimes="0;1" dur="3" keySplines="0.2 0 0.8 1" begin="0s" repeatCount="indefinite" />
    </circle>
  </svg>
</div>

<ul class="filter activities">
  <li id="filter-Reading" class="filter">Reading ({{ site.cards | where: "group", "Reading" | where: "topic", "Defining Data" | size }})
  </li>
</ul>

<ul class="filter topics">
  <li id="filter-Defining-Data" class="filter">Defining Data ({{ site.cards | where: "topic", "Defining Data" | size }})
  </li>
</ul>

<div id="filter-none">{{site.data.snippets.reset-button[page.lang]}} ({{ site.cards | size  }})</div>

<!--
this div ('lesson-list', referenced in lessonfilter.js) needs to contain the sort button/elements AND the actual list for the sort buttons to work
-->
<div id="search-div" style="text-align: center; margin-bottom: 1rem; display: none;">
  <input id="loading-search" class="search-input" type="text"
    placeholder="{{ site.data.snippets.loading-search[page.lang] }}" style="background-color: #efefef" disabled>
  <input id="search" class="search-input" type="text" style="display: none;" placeholder="{{ site.data.snippets.type-search-terms[page.lang] }}">
  <button id="search-button" disabled>{{ site.data.snippets.search-lessons[page.lang] }}</button>
  <i id="search-info-button" class="fas fa-question-circle"></i>
  <div id="search-info">
    {{ site.data.snippets.search-info[page.lang] | markdownify }}
  </div>
</div>
<div id="enable-search-div" style="text-align: center; margin-bottom: 1rem;">
  <button id="enable-search-button" style="width: 100%;">{{ site.data.snippets.start-searching[page.lang] }}</button>
</div>


<div id="lesson-list">
  <!-- List.js uses button classes of asc and desc to control sorting functionality. -->
  <ul class="sort-by">
    <li id="sort-by-date" class="sort" data-sort="date">Sort by Date</li>
    <li id="sort-by-difficulty" class="sort" data-sort="difficulty">Sort by Difficulty</li>
  </ul>

  <!-- Display the current filter and sorting criteria -->
  <h2 class="results-title">Filtering Results: <span id="results-value">All Lessons</span> <span id="current-sort" class="sort-desc">Date</span></h2>

  <!-- List of lessons -->
  <ul class="list">
    {% for lesson in alllessons %}
    <li>
      <!-- Display information about each lesson -->
      <p>Title: {{ lesson.title }}</p>
      <p>Author: {{ lesson.profile.author }}</p> <!-- Assuming the author is specified in card.profile.author -->
      <!-- Add more fields as needed -->
    </li>
    {% endfor %}
  </ul>
</div>


<script src='//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src='//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js'></script>
<script src="{{ site.baseurl }}/js/URI.min.js"></script>
<script src="https://unpkg.com/lunr/lunr.js"></script>
<script src="{{ site.baseurl }}/js/vendor/lunr.stemmer.support.js"></script>
{% if page.lang != "en" %}
  <script src="{{ site.baseurl }}/js/vendor/lunr.{{page.lang}}.js"></script>
{% endif %}
<script src="{{ site.baseurl }}/js/lessonfilter.js"></script>

<script>
  $(function () {
    wireButtons();
  });
</script>
