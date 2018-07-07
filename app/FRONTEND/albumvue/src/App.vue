<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper black">
        <img src="../static/logo.png" class='navImg center'/>
        <a class="brand-logo right logo">Wedding Picture</a>
        <ul id="nav-mobile" class="left hide-on-med-and-down">
          <li><router-link to="/">Public</router-link></li>
          <li><router-link to="/Approving">Approve</router-link></li>
          <li><router-link to="/Upload">Upload</router-link></li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css";
@import "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js";
@import "https://fonts.googleapis.com/icon?family=Material+Icons";

.navImg {
  width: 70px;
  margin-left: 33%;
  margin-top: 10px; 
}

a.logo {
  font-family: 'Courier New', Courier, monospace
}

</style>
