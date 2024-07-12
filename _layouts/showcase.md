---
layout: default
---

<div class="page">
  <header class="page-header">
    <h1 class="page-title">{{ page.title }}</h1>
    <h3><i class="fa-solid fa-people-group"></i><b>&nbsp; Contributors:</b> {{ page.metadata.contributors | replace: '<br />', ', ' }}</h3>
    <div class="row no-gutters">
      <div class="team col-sm-8 col-md-7">
        <div class="card-body">
          <p class="post-description" style="font-size: 10px">{{ page.teaser }}</p>
          <p></p><small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ page.metadata.source }}">{{ page.metadata.source }}</a></small></p>
        </div>
      </div>
      <div class="col-sm-4 col-md-5">
        <img src="{{ '/assets/img/' | append: page.metadata.image | relative_url }}" class="card-img img-fluid" alt="{{ page.metadata.caption }}" />
        <div class="card-body" style="margin: 2px;">
          <p class="card-text">
            <small><b>&nbsp; Caption:</b> {{ page.metadata.caption | replace: '<br />', ', ' }}</small> 
            <sl-button-group label="Alignment">
              <sl-button>Genre: {{ page.metadata.genre | replace: '<br />', ', ' }}</sl-button>
              <sl-button>File Type: {{ page.metadata.filetype | replace: '<br />', ', ' }}</sl-button>
              <sl-button>Topic: {{ page.metadata.topic | replace: '<br />', ', ' }}</sl-button>
            </sl-button-group>
        </div>
      </div>
    </div>
  </header>

  <br />

  <article>{{ content }}</article>
</div>
