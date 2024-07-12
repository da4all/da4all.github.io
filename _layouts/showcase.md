---
layout: default
---

<style>
  hr.rounded {
  border-top: 5px solid #bbb;
  border-radius: 5px;
}
</style>

<div class="page">
  <header class="page-header">
    <h1 class="page-title">{{ page.title }}</h1>
    <h4><b>Contributors:</b> {{ page.metadata.contributors | replace: '<br />', ', ' }}</h4>
  </header>

  <br>

  <article>{{ content }}</article>

  <br>
  <hr class="rounded">
  <br>

  <h2>Project Details:</h2>

    <div class="row no-gutters">
      <div class="team col-sm-8 col-md-7">
        <div class="card-body">
          <p class="post-description" style="font-size: 14px">{{ page.teaser }}</p>
        </div>
      </div>
      <div class="col-sm-4 col-md-5">
      <div class="page-info" style="background-color: #f2f2f2; padding: 10px">
      <img src="{{ '/assets/img/' | append: page.metadata.image | relative_url }}" class="card-img img-fluid" alt="{{ page.metadata.caption }}" /><br>
        <div class="card-body" style="margin: 2px;">
          <p style="font-size: 12px">
            <b>Caption:</b> {{ page.metadata.caption | replace: '<br />', ', ' }}
            </p>
            </div>
            <sl-button-group label="Alignment">
              <sl-button>Genre: {{ page.metadata.genre | replace: '<br />', ', ' }}</sl-button>
              <sl-button>File Type: {{ page.metadata.filetype | replace: '<br />', ', ' }}</sl-button>
              <sl-button>Topic: {{ page.metadata.topic | replace: '<br />', ', ' }}</sl-button>
            </sl-button-group>
            <p><small class="test-muted"><i class="fa-solid fa-link"></i><b>&nbsp; Also Published Here:</b> <a href="{{ page.metadata.source }}">{{ page.metadata.source }}</a></small></p>
        </div>
      </div>
    </div>
    
</div>
