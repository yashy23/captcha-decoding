<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>yash</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Breaking-a-CAPTCHA-system">Breaking a CAPTCHA system<a class="anchor-link" href="#Breaking-a-CAPTCHA-system">&#182;</a></h1><p>Ref: <a href="https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710">https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%</span><span class="nx">javascript</span>
<span class="nx">IPython</span><span class="p">.</span><span class="nx">notebook</span><span class="p">.</span><span class="nx">clear_all_output</span><span class="p">();</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>





<div id="009239a7-3433-45ec-9a2b-c6903abd02b9"></div>
<div class="output_subarea output_javascript ">
<script type="text/javascript">
var element = $('#009239a7-3433-45ec-9a2b-c6903abd02b9');
IPython.notebook.clear_all_output();
</script>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[160]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">simplefilter</span><span class="p">(</span><span class="n">action</span><span class="o">=</span><span class="s1">&#39;ignore&#39;</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">FutureWarning</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Install some packages below (if not installed already):</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">!</span>pip install opencv-python
<span class="o">!</span>pip install imutils
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In this exercise you will break <code>Really Simple CAPTCHA</code> plugin of WordPress: <a href="https://wordpress.org/plugins/really-simple-captcha/">https://wordpress.org/plugins/really-simple-captcha/</a></p>
<p>Try a demo here: <a href="https://contactform7.com/captcha/">https://contactform7.com/captcha/</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The plugin generates 4-letter CAPTCHAs using a random mix of four different fonts. Letters are from 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789' and "O", "I" and "1" are not used to avoid user confusion. That leaves us with a total of 32 possible letters and numbers that we need to recognize.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Since we have the source code to the WordPress plug-in, we can modify it to save out CAPTCHA images along with the expected answer for each image. We generated 9955 images under folder <code>generated_captcha_images</code>. Run the following code to show 10 images to take a look.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">CAPTCHA_IMAGE_FOLDER</span> <span class="o">=</span> <span class="s2">&quot;generated_captcha_images&quot;</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-1:-Extract-single-letters-from-CAPTCHA-images">Step 1: Extract single letters from CAPTCHA images<a class="anchor-link" href="#Step-1:-Extract-single-letters-from-CAPTCHA-images">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Run-the-following-code-to-show-10-images-to-take-a-look.">Run the following code to show 10 images to take a look.<a class="anchor-link" href="#Run-the-following-code-to-show-10-images-to-take-a-look.">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>
<span class="kn">import</span> <span class="nn">glob</span> <span class="c1"># glob.glob returns the list of files with their full path, and it supports wildcards</span>

<span class="kn">from</span> <span class="nn">IPython.display</span> <span class="k">import</span> <span class="n">Image</span>

<span class="n">captcha_image_files</span> <span class="o">=</span> <span class="n">glob</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">CAPTCHA_IMAGE_FOLDER</span><span class="p">,</span> <span class="s2">&quot;*&quot;</span><span class="p">))</span>

<span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">captcha_image_file</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">captcha_image_files</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">i</span><span class="o">==</span><span class="mi">10</span><span class="p">:</span> <span class="k">break</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">captcha_image_file</span><span class="p">)</span>
    <span class="n">display</span><span class="p">(</span><span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="n">captcha_image_file</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\222X.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAADqklEQVRYhe2YQUgqQRzG/w2LLbEH
WZZlMQkPEhGySHjsJJ0iQjxEh04dRCLsah7Cg3SQ8CASISIhEuJBJEQ6RYhILHsQDxIRUuIpRGKx
JZaFeYflSbx09OHrPXr0OznjNzPfN/ufcXEGYwz/I+hfG/gsvoN9NahRXzw9PcXj8YeHh6WlpUAg
MD8//zdtAcDBwcH19bUgCDzPOxyOw8PD19fXQY8gCLOzs6TxeBipVIrn+WQymU6nWZa1WCyKogxV
fh7tdtvr9QLA8vLy+fk5xvjx8VEURcM2QkjTNMLwIcEkSUIIHR8fG81wOAwA5XL5M9yTURTFYrEI
gvDy8mL0VCoVhNDZ2dnYjR4SrNlsJpPJwVynp6cAUCwW/6zpCbm4uAAAn8+HMW6324IghMPhSQYO
L8X3bG9vMwzT6/Wm9Ygxxrjf70ejUafTyTAMx3E+n+/t7Y08xO12I4Surq6cTqfX651woTHBZFmm
KCoajRI0mqZFIhGr1cowzObm5uBRf6Tb7TqdToRQrVaTJMk4LYlEguzh7u7OZDIhhERR7Pf7ZPEA
UjBFURYXF91ut67rozSapq2trfn9fkVREokEAEQikVHiUCgEAKIoYoxVVTWCDQ4zgZWVlUm24D2k
YBsbGzab7fn5maA5OTmhKKrb7WKMe70eAIRCoVFiWZbL5bKqqvjn4UEINZtNssVgMMj/hFAOvzAy
WCAQMJvNY1et1+utVsv4XCqVAECSpLGrqqpqt9sBYH9/n6zM5/M0TVer1UwmAwB7e3tjJzcYHiwW
i9E0fXNzYzQ7nQ75RwNjrOu6y+Xa2dmZZNXd3V0AcLlc5Juj0WgwDJNOp42mcYtMsnF4aLBsNktR
VD6ff++DXJAY43A4bLfbJymVWCwGADabrdPpjNLoui7Lss1me/9IjVvE5XKNXQJ/DKZp2tzcHE3T
oiiurq6ur697PB6GYcizFAoFlmUbjcbY9XK5HEKI5/n7+3uCzOPxGFfLwsJCoVAwOrPZrNVqBYBg
MGgcVAJDnli32221WvV6vVqtlsvlfD6fy+UIU1SrVZZlK5XKuFD48vLSZDKxLFuv1zHG/X5/a2tr
qFJV1VardXt7WywWB+fc5/O53W6Hw8Hz/NHR0W8H+y0kSeI4rlQqGc1UKjVKWSqVaJo2m82yLBs9
sVjM7/dPaWAUUwWr1Wocxw1KpdFoGO8+HzEq/OMreCaTmcYAgamCcRz3i9F4PP6nnE3JDP7+z+Nr
8R3sq/EDJN4GUCIZ2HMAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\226U.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAAEKElEQVRYhe1XT0gqexQ+t0YrUath
EAsLAwkRMQmREJGQEBcSFRIh0apAWkZIRIiERKtWIeEiWkSQULSSEIsWg5SQgYpIhBmIqNgfTMLM
mrsYnvjKmYl7333v3bjfaub8Ps583/nN75yZbwRBwFdEw38t4Ffhj7HfDV/WGEKz9vr66vP5QqFQ
sViUyWRms7mlpeVfU/azICgQjUZ7e3sxDFtbW1OpVADQ399fqVSo+CQSiUQ4HGak/Rii0ajH43E4
HBMTEycnJ/RkSmPd3d0AsLy8TBCEy+Uiq5BIJKj4OI5rNBqVSiUQCDAM83q9n5Qbi8Xi8fi7YD6f
x3Hc7XbPzc253W4yaLFYuFwuACwuLpbL5R80ZrfbNzc37+7uCIKYmpoCAAzDqLbC5/Ox2eyVlRWC
IIrFolgsxjCsVCrRPLhQKKyurorF4rGxscPDw9ql7e1tDodDllKlUtXaXl9fB4CdnR16V3TGqggG
gwiCAMDGxgYVx+12W63Wh4cH8tZisQBAKpWi4sdiMYlEotPprq6u6hIKhUJDQwMATE9P18b9fj8A
LC0tMcpmMJZOp8l3cnJykjFXFWq1uq2tjWp7k8kkiqIGg4H+KEokEgDQarW1wVQqBQBms5lRA52x
fD4vl8sBYGRk5PP9wOfzAYDT6aQiDAwMCIXC6vZSwWQyAQCKou/ifD5fLpczyqA0lsvlFAoFAIyP
jzOe1CqSyaRAINDr9VSF8Hq9AGCz2Vwul8PhCAQCVKlsNht5zHK5XG1crVaz2WzGQtcf0Dc3N1qt
NhwOW63W3d1dFot1dHTEODmy2azBYBCJRAcHB42NjXU5brcbAMLh8NPTUygU0mq1e3t7dZlSqZS8
iMfj7+LlcjmdTjOo+eg1FAoJhUL4q9cTBJFOp5VKJX2FUqmUVCpVqVRkI6WCQCAYHBwkr8vlMp/P
Hx4erss8PT0lFb5rWna7HQBisRi9njo7ptfrM5kMh8Px+/2jo6MzMzNGo9FgMNBU5/r6WqfTYRh2
fHzc3t5ORbu/v6++4QDAYrG4XC7Zcj9CJpORjbHqkASHw0EQRCQS0eiBup9UmUzm7u+QSqXkUa6L
SCRiNBoVCsX+/j75zXV+fo6iaE9PzzsmOV5JuQCQzWYzmYzRaKyblsfjaTQaHMd9Pt/LywuLxSLj
sVjMYDDweDx6Y8xzjBEYhiEIYrPZtra2cBxPpVImkymZTNYl63Q6pVJJHv35+XmlUkkzxwOBQHNz
MwDMzs6SNL/f39nZeXl5yajqG/HTf9AXFxfxePyqBpVK5fb2ti45EokMDQ0JBAIURd/e3jweT0dH
B03ys7OzhYUFHMcRBBEKhTqdzul0dnV1Mar6B4x9xPPzc1NTE9Xq4+NjMBjEMKyvr+/zCUulUmtr
6+c1/BJj/wd82R/NP8Z+N3wHULER8VD8kNAAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\2274.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAADeElEQVRYhe2XQUjqcBzHf2/Enxox
OgwJ6VAhMWpEiIhIRARJSUiHEAkPIjIIOnTq0EEiRogH6bQoooNIB7tFBXWo8CASITKi05AYYRId
ZIjIMP7vIEjP3Jz0eo8X73Ny7Pv//f4f/v7/235gjOE7QvztCXwV/8X+Nf6L/Wt0fb7ExcXF5eXl
09MTSZJer3d+fv7zNX8D+BM8Pj7a7fbh4eFIJMIwTL1gOp3+TE0tVFXtKK8nJopiNBoVBOHl5eXj
3VqtxrIsAMTjcYxxKpWqiwmC0NEM2qKq6tra2tTUVEejWoupqhoIBGZmZnieHxgYoGm6WCw2ZfL5
PACYTKZUKoUxliSpLiaKok6/arXKcdz6+rogCOfn5w8PD5VKRX+K29vbAOB2uzvx0hALBoNms7la
rWKME4kEAJycnHyMXV1d1TMY44ODAwDweDz6/SKRiNVq3draCoVCLpeLYRiEEE3TR0dHLfP5fJ4k
SYRQKBTqQEtLLBaLZTKZxm+CICRJ0i/EsixFUbIs68fC4XCpVGpcSpJEkuTo6KjWurnd7oWFBYvF
srm5qV+5iTaHR7lcHhwcDAQC+rH6ctU3m3FqtZrT6UQI5XK5loFkMknTdKFQQAjt7+93VLyNmM/n
m5iYKJfLOpnX11eapv1+f/2S47jT01MjvXmeB4BoNNryrqIoZrM5mUwWCgUAMFizgZ7Y6uoqwzAt
j8T3BINBhmEa8k6n08jBeHd3hxCanJzU6e7z+TDGmUwGALRWVQtNMY7jxsfHPx6GTdzc3ADA4uKi
z+ez2Wx9fX0AsLGxoT9KUZSRkRGSJLW27u3tbX9/vyzLpVLp8PAQALLZbK1Wa+vToIVYpVLxeDzT
09P1Xa4oitbgSqVisVianvgURYXDYf2uXq8XAHZ2drQCLperq6uLJEmKorq7uwmCcDgcbf8772kW
k2XZarX6/f7Gk17n5Mhms3a7fXl5ORwOx+PxdDptpHcsFgMAh8NhcIocx7EsazDc4Af+9Qt6aGhI
lmWbzWYymUwmU7Va7e3t3dvb+11vcNfX1y6XiyCIbDY7NjZmZMjs7CxC6OzsrKNGzS/B9/f3xWLx
5R1zc3MdVdTh+fl5aWmJIAie541YHR8fJxKJXC5HUdTu7u7KyorxXs0r9qW8vb2JosgwTE9Pz1f3
+qNif5Jv+6H5bcV+AgL/O2IsrREpAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22A6.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAAD9klEQVRYhe2YQUgqXRiGvzuYiNhg
mxYiNInIIIO4kIEuISZlEa1ExFWIRISEhLiICAmJWUS0aBERIdJCxE0tIqVFSEhIiAsXQiIiwzCI
kZREiQXnXwxIlI7SvRH93HflOfPOe85zzjeHGX8hhOD/KOy7J/BV+k6w5+fnrwv/HrDb29vp6Wmn
0/mFY6DuOj8/93g8NE3PzMxcXl6KONtiWTYSicRisVqtJmIbHx8XRo/H4/3EfkKdwVqtltPpJAgi
HA4bDAYAUKlU4kGtVsvr9ZIk6fV6CYJQKpWZTKabWalUCmAqler+/v6PCLqoM5jf7wcAhmEQQtvb
2wCAYViz2RQJcrlccrm8Wq0ihCqVCoZhc3NzHZ2NRgMAvF6vwLa0tNTnXDmO29nZcTqd4XC4p7kz
mEajIQhCKL/V1VUAMBgM4kHBYDAWi7WbSqXSZDJ1dBYKBQDIZDIul0tYsqurK/HwRqOxuLgolUr1
ej3DMCzLivtRN7Bisfj6+ir81mq1ALC3t9czq61yuSzsSceryWQSAFiWrVarQk1SFNVqtbqlcRwn
PA6BQEDE9k5ihwdCKB6PA4BOp+s/ESHkcrlwHO+2roeHhxiGtVqter3udruFgtzc3Oxofn19NZlM
ALCwsND/BJA4WLPZ1Gg0AJBMJvtPPDg4AIC3ZflOGxsbEolEp9PhOG42m4XdkMlkpVLpo3lrawsA
cBx/fHzsfw5IHGx9fR0A3G53/3FnZ2cSiaTb8gvyeDxGozGfzwvNUqkkk8kAwGq1fjQTBAEANE3b
7XatVmu1WtPpdD8z6QqWy+WkUqlara7X6wihYDB4cnIinpVKpeRyeSAQELfZbLb5+fm3PaFQSCjI
UCj0toCz2azQbzab8/k8wzAAoFAoOI77JFiz2aQoCsOwi4sLocdisaRSKZGgdDqtUCh8Pl/PIUmS
XFtbazcbjYZw9Mvl8t+/f0cikfalaDQqgJXLZYQQz/NCMxqNfhJMGImiKJ/PZ7PZVCqVXC4vFAoi
VDiOLy8vt3uOjo6KxeJHJ8uyMpnMaDSurKy0wfb393O5XPscbmt3d1cgEaqmUqkIzX6e+V/ow2fL
3d0dRVE6nY4kSZIk9Xo9SZIjIyMi72VDQ0NPT08Oh0OtVqvV6uHh4WAwmM1mBwcH39oeHh5omqYo
iqZpmqYnJiZEMgEgkUjMzs4KOzY6Onp8fGy321UqVaVSGRgYEL+3A9gndHNzw7Isz/Mcx/E8z/N8
s9lMJBJ/njw2NpbJZBiG8fv9k5OT19fXp6enU1NTve/suaffq1qt5nA4JBKJQqGwWCw931Ha+js7
9tV6eXnpWXvv9DPAPqF/fw38NP0D+2n6D1q+v7Vjz8NAAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22BJ.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAADqklEQVRYhe1YQUgiURj+dxrEJAYy
GhwiiTARiQoPESnRIUgKQjoESRhEQUREhIR0CE8yB0/RISLs0slLBtEhOkhIhygoijGmDnMQMVOR
OQxWwtvDA3HXmVF3XZaN/Q7yfuZ733vf//73j/oNIQRfEcTf3sCfwn9j/xoaZuzt7W1paamtra21
tXV2djabzTZE9vn5mWGYzs7Onp6e/v5+u93++flZ00zUCPA8T9M0y7L5fH5nZwcAFhcXG6KMEBJF
0Wq1AoDD4UgmkzXOaoyx0dFRmqZLocFgMJvNDVHGoGkaAPx+f+1TyIYUjNfr7e3tLYUkSVIU1RBl
AMhms+l0GgDKl6gKNWPxePz09FQQBI1G43Q6x8fHlZiTk5Ol8f39fSKR2NjYkGUeHx8fHR3xPJ/J
ZDQaTbFYtFgsHo9nfn5eSfzx8REP6jImX4qSJM3NzVEUtba2ZrPZMDMcDtdSA06n02QyFQoF2afp
dPr8/BwAfD4fQiiVSrndbgAIBAJKgru7uwCg1WqLxWItG8CQNzYzMwMAm5ubCKFkMomNraysVJU7
ODggSTIWi6lwYrFYyRhCKJPJAMDExIQSf3l5GQAGBgaqrl4O+XYfiUR0Oh3uRQzDaLVaABgaGlI/
/Hg8vr6+vr29bbfbay8ZURTVxXEp1leHoFCKl5eX+Xy+PMEmk+nj40MlQ6IoWiwWlcSXUDoxSZKu
rq6Gh4fdbrdS6SKE9Ho9ALAsW1W5HNXbvcvlIggiGo2q06anp81mcykdoVBIiYmNlUAQhMPhuLm5
kSWXLsLZ2VnVrZajirFoNApl90EJfr+foiiO43AoSZLNZlMil98xURT39vZaWlp0Ot3Ly0slGXca
kiRzuVwVKz9CzVihULBarSMjI7gdBYPBSCRSSZMkSaPR/FTh5e9rFWMY+MvK6upqJZllWQBwu911
eEIIKTUPDL/fn8vlwuFwU1MTAFxfXz89PVXSmpub39/ff9J9fX2t/Z67XC4A4Diu8tHFxQVN08Fg
sHY1DMUX9O3tbTAYnJqaYllWEARBEO7u7oxGY70L1ALc8bu7u3F4eHgYCoX29/dTqVQikYhGowzD
1C0qe46FQkG2vS4sLNRbEpXApej1enHI8/zg4KBer+d5HiHEcRwO+/r6AoGAJEm/tso3JPfXwMPD
g8fjMRqNXV1d+BMP2tvb687cjzg5Odna2uI4jiAIg8EAABRFjY2N+Xy+jo6O3xQvh7yxL4D/v6D/
NXxZY98B5M0M0i8VXeYAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22HS.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAAELklEQVRYhe1XTUgyaxQ+3zDaECIm
IiRhIhIiEgYiEiEtRFpYCxFyHSQV9oOY7SJCWpiLCAlrJRLiIkIiaiMlEv0QtLCIFlNEhI2TDBI2
RI3MXcxFxH++e+93+eJ7dufxec97Hue85535wbIsfEcg/3cB/xX+GPvd8G2Nob94v+vra4/Hg2FY
V1eXTCbzer08Hu/r66tQKHR0dFTri8ViJBLZ39/PZDIYhvX09Fit1uHh4eY7sb8c6XQaAEwmE47j
HEMQhMPhaG9vV6lUNpuNJEmOp2l6YGBAKpWenp4SBLG0tAQAUqmUYZimuzQyRtN0KBSamJjw+XxP
T0//3BKHk5MTAPB4POVkoVDg3JaTy8vLAGCxWEqM0+nc2NhoZZe6Z+zy8lKtVuM4rlarg8GgTqd7
eXn5ufarQCaTAQCZTFZOPj8/A4BKpSonb25uACCVSh0eHnLM5ubm5ORkK7vUNvb6+mo2m41G4+rq
6uzsbCAQoCgqFovVy3J2djY6OtrZ2dnW1tbd3T09Pf3+/l5PzHmoMFbTrcViAYCPjw+r1To+Pp7N
Zlux9DdqPkeCIPx+/+PjIxcmk0kAWFlZqSkOhUIIgmg0GoIg4vE4l9blctVrEo/HAwB2u93v90ej
0WQyieP41tYWAIRCoQqx0+kslSoQCNbW1lrpQ7bxGSvB5/MBwPn5ec1fhUIhAExNTXGhWCwGAJvN
Vi+bw+EAgMXFRbfb7XA4BgYGlEolhmEAsLe3V60/ODjQarUle3Nzc63U3NwYQRASicRut9cTRCKR
ZDLJTSqSJBEEAYDd3d16epPJxDVYOTkzMwMAV1dX9VYFg0HOPIIg6XS6adlNjDEMYzabFQpFLpdr
motlWbfbzbVZA41SqZRIJBWkzWYDgNKg5xCNRmmaLoVcuwLAzs5O00qaGHO5XEKhsJV/iGXZVCqF
oqjRaCyvphoYhvX29laQRqORz+dXkEKhMBgMlkJu6iAIUroAG6CRMb/fz+fzE4lE0ywsy2YyGZlM
ptPpKIpqIMvlcgAwNDRUwcvlcoVCUc7QNM0NjGQyyTHcE3O73a3UU9dYOBxGUTQWi3Hh29tbgyw0
Tev1eq1Wy/VSoVCoLp1l2aOjo5GREQDQarV3d3cl/vPzk8/n9/f3l4sZhhkbG5PL5QiCGAwGvV6v
UqlavJ3rGovH4yiKlg9fr9f78PBQL4vNZtNoNKUTEovFtFpttYym6dvb20QiEQ6HS8lTqZRer0dR
VCQSra+vV6/K5/M4jrd4yEv4wVZ9QReLRZFIxDCMwWAQi8UikUggEGxvb5MkyePxqm/C+fn5QCBQ
QRoMhouLi9av02KxSJIkQRB9fX2tr2qAGsYAIJvNkiRJUVQ+n6coiqIohmEWFhaqlff39xXvQRwG
BwePj4//lRJ/DrWNfQN82w/NP8Z+N/wFhcCPdRrIvRAAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22KD.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAAEfUlEQVRYhe1XXyhzfxh/3uNYrDmd
1pJmrTVai10tMZGyJNYICReSJK2luWEtIblwIbnAhdaSJJYLudBCyMUutOQCzZ+kWZKGmWMmB/u+
F6fWeWf/vOX1+729n4t1nmfP93mez/f7Oc+38wMhBH8jsO9u4Kvwj9g34eXl5f7+/v39/bML/xCx
m5ubg4ODzc3NhYWFg4MDAOjq6qqqqiooKMjKylpbWwuL7+npKSwsTEtLUygUSqWSx+PV1taenJx8
oiT6ehiNRhzHmXIqlWpvbw8hZLVaAYAkyf39/Y9Lbm9vDQYDAHi9XoSQw+GQSCQEQTidzgSL/gli
CKGlpSWG2NLSEuMpLy/HMMxms0VbUlNTQxBEyNza2gIAjUaTYEU84jFeXFyMj4+fnZ3J5XKDwZCZ
mRnjzB8eHiwWi91upyhKLBZrNJq6urqkpCR2jEQiYR48Hg8ATExMrK+vDw8PV1ZWRkvrdrvFYnHI
LC0tzcnJ2djYeH5+Tk1NjS1DgEhStFgs6enpZrN5enqaz+cLhUKKoqJtjNfrlUqlAKBWq7e3t7Va
LQDk5eX5/X522OXlJVNuaGjI6XRyudz6+vrYWy4QCLRaLdtTV1cHAMfHx4mcWDgxh8OBYdjw8DBj
Dg4OAkAMwdjtdi6Xm5GRYbfbEUI2m40hMDMzww6jaZrx63Q6pVKpUCjCmIfB7/cDgF6vZztbW1sB
4Pz8PBFi4VLk8XhTU1MNDQ2MmZ6eDgChtj6iqKjo6ekpZB4fHzMPbBUBQHJyMkmSPp9vcXHR6/WK
RCKXy5WbmxstrdvtBpaAGVxfX+M4npGREW3VL4jNu6mpicfjMaMpLk5PT/l8PgC0t7d//FcmkwFA
SUmJ0WgEAJIkt7e3o6VaXV0FAKvVGvLQNE0QRHFxcSKdoNhTcXd3F8fxkZGRRBIdHh6KRCIMw0wm
U8SA4uJiAJDL5Qihjo4OAOBwOOzW2TCbzQCws7MT8szOzsIHhcdAVGIURclkMrVa/fb2FjfLysoK
QRAikWh1dTVaTH19PQDw+XzGZNSOYdjo6OjH4N7eXgC4urpiTI/HIxKJ8vPz43YSQlRiWq1WIpF4
PJ64KQYGBjAMa2lp8fl8CKFAIBAxTK/XM0yYnaJpuqKignkdWlpa5ufn2cHNzc0YhgUCAZqmt7a2
cnJyFApFIs3EIWYwGEiSjHvNezyesrIyDofDVohOp4soMGamAUBfX5/L5UIIBQKBkpISAMjOzp6c
nGSz4vF4XC5XIBAIhUKlUjkyMkLTdOKsIhMbGxtLSUkJvdmXl5cRk/p8PqFQGBpCEomkoaGhu7sb
x/GPE7mzs1MqlapUqurq6o6ODuZuQAjRNJ3g+P4swonNzc3hOL64uBjytLW1RdPA8vKyyWRSq9UE
QYQYisXir2j0s/iBWF/Qr6+vJEkGg0GZTEYQBEEQHA5nY2Pj8fEx7rVxdHS0s7PjcDiEQmF/f39C
V81X4hdiAHB3d0dRFEVRfr+f+Q0Gg42Njd/V328jnNhfg//6F/Rv4x+x/xt+AloULbvqmTSbAAAA
AElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22L9.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAADmElEQVRYhe1Xz0vjQBidDUH7A6GU
EErIIYqUImkJUnsoUiV4EJHqwWORIiiSk4iIF6uIhCL+AR6KFE/Fg4cKRXrQS29iCxVBimiQWGJo
PZQSq0SyhyxLt9VJhC67K/tOM5P3vfleJvNN5pumaeArAvnTCfwu/Df2r+HLGkM7qPX4+JhOpxVF
YVnW6/VCmMfHx/F43Gaz4Tju8XjW19c7mMYPaB1CKpXq7++fnZ0lCAJBkHQ6DecfHh4CADiOUxSl
Uzk0w6yx29vbYrGoquq7T09OTlAULZVKmqYJgoCiaCgUggsmEgkAQDKZNDN7rVZbXl4mSRLH8ZWV
lY/SaIaxsVwuFwwG/X4/juMYhmUymXbO8PAwwzA/uz6fj6IouCzP8wCAd9Va0Gg0AoFALBar1+tb
W1sAgEQiYRhlYCybzXZ1dfE8r2lavV6nKArDsEaj0UIrFovNXxRFUeFwGK68tLQEAMjn84YpxmIx
j8ejtxVFQRBkZmbGMMqgKgqCMDc3x3EcAMButweDwUqlUqlUWmher9dqtert8/NzPQquLEkSAADH
ccMqsL+/HwqF9LbVanU4HO0JtMOgKs7Pzzd3b25uHA6Hy+WChPA8zzDM1NQUXFmWZWDC2NvbW7lc
bh5RFAXDMHgUAJ+pitlsFgCwvb0N4eRyOQDA6empoRpN006n08y8NE27XK5SqSTLciQSAQDs7u4a
Rpk1JggCjuMsy0IqkqqqDMNEIhEzgvoJZoaZz+f9fr/FYgkEAtFoFEVRQRAMo0wZkyTJ7XYPDg7W
ajUILR6PO51OWZb1LmTdVFVFEGR0dNTM7D/x+vpK0zTHcWbIxsZEUfR4PH6//+npCUIrlUoWi+Xg
4EDvqqo6MTHxEVmvHNPT082Da2trlUoFMkU0Gg0GgyYP9G8a9D52d3c3NjZGEEQmk+np6YEwR0ZG
7u/vNzc3RVEURVE/AAqFQjvz7OxsZ2dHP9PD4bDb7cYwrFwup1Kph4eHd8Wvrq4WFxcpitrb27Pb
7caVAwCYscvLy/HxcZ/Pd3R0pFfzi4sLp9PZ29vbwqxWqyzL4jhOkiRBEARBkCTZ19f37h/j8/Nz
uVyWf4UkSQMDAxsbG+2WeJ632WwLCwtDQ0NmLP0AZDUxDENRdHV1NZlM5nI5URQnJyfNbNy/AbAV
KxQK19fXN01QVbVarX7itf05GOyxFry8vHR3d/++bDqIzxn7h/Blb9Bf1th3Khp1cx0tmzYAAAAA
SUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22NR.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAAEdElEQVRYhd2YT0gqXxTHz5PBSiRi
kGEYZLA/mESEREXI4CIkXIhYCwmJiJCIFiHRwlqEq4gWEhEmEuHCRUmEuBCLlhISISERFS4iYggJ
KdEQmdf9LS5viLLRfvV60Hd3DueeOR/m3nPuzC+EEPxEyf51AX9LPxaM+NcFvKvHx8dkMnl0dHR6
eprNZmUymV6vn52dbW1trWk9el+CIGQymVwuJxHzN5RMJq1Wq1wuBwCbzRaJRDwej1KpBACVSlUo
FGpJ8i5YKBTSaDQqlQoAHA6HIAhfV3kVpVKp7e1tgiAAwOl0Yufa2hp+E5FIpJYklcGWlpZYlr27
u0MIOZ1OAAiFQl9Vd41qa2sDAIPBgM1EIoHBYrFYLcsrgPE8L5PJZmdnsZlKpQBgbm7uqyquUVar
FQBIksSmz+cDALVaXSqValleoXmQJBmPxwcGBrBZLpdxRomD+vv370QicXV19fz83N3d3dvbKxG8
v7/v9XoZhvH5fA0NDdhZLBbv7+8pihI9Op0uGo3mcrmdnZ10Or26usowzN7eXl1dXfXOAZLNA2th
YaG+vp7n+fcCdnd31Wq1wWDgOA7nXFhYkM45NzcHAIFAQPRcX18PDg4SBDE2Nvbw8IAQ2trawtka
GxtpmgYAi8VSLpdreV1Ionlg8TyvVColCt3b25PJZCzL4u7S1dUFAAzDSKe12+0A0NXV9dK5vr5u
t9tFM5lMYjC/318oFDo6OgDAbDY/PT1Vx6oKNjw8rNVqJba1zWYDAKvVis2RkREA4DhOOq1arcZs
iURCdDocjtXVVdF8eHjAYC6XCyF0dnamUCgAwGg05vP5T4EFg0GCII6PjyVi0un02dmZaLIsC9Ua
183NTWNjI8/zcrl8ZGRE9Gs0mlfPYhgGAAYHB7G5ubmJUXt6elKp1P39/f8By2QySqVyeXlZYvEr
hUIhABgfH5cOC4fDJpMJIeRwOORyOR4qPM8rFIpXRwg3MJZlRY/D4cBsCoVCegJVBiuVSnq93mw2
i56ZmRnpcnO5HE3TnZ2dVW8GLpdrcXER/RlNHo8H0xqNxpdh5XLZZDJhDLPZfHJyghAqFAput9vn
81W9D1UGm5ycJEny5OTk4uIilUrF43GtViudaHR0lCTJTCaDEEomkwcHB+9F9vX1iXtVr9czDCMI
gsvlcrvdL8Omp6c5jpucnPR6vbFY7KM3uwpg+XxepVLRNK3RaDo6Orq7uzmOe3kY3iocDhMEcXh4
iM2lpSV84t+qVCrV19eLVQYCAQAIh8N9fX3RaPRDpUur+hyrqpubG5IkLRaL3+/3eDxTU1MURU1M
TFQMTiQSOp1ONJ+enpqamvr7++VyuXQz+Kg+CyYIgtFofDv3X06kl1pZWXnF7HK5AKDqVv+oPvs9
dn5+fnt729/fT1EUTdPUH+l0urfB8/PzwWCwpaXl8vKyvb0dO6enp9fW1gwGwycreaVf6Bv/eRSL
xWw2m81mKYpqbm4W/RsbGzRNDw0NfeGzvhXsO/Vj/3n8WLD/AHFuNDdzswpzAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>generated_captcha_images\22PL.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAYCAIAAADWASznAAADrklEQVRYhe1XTUgqbRQ+dxhfRFxI
mIi2KJGIkClEJKIIoiCEokWESLgaWkgLC4mwaNGqxRARIREtIsJVhEmYm0LChUgM0aJEoiAiSqJo
GMoGae7ivfR9N2emye+7f3GfxTBzeM55z3POeQ/MF1EU4TOC+NUJ/Ch8WmHkr05AFjc3NxzHcRzH
83xHR8dH3X/Tjj0/P09PTzc0NHg8ntPT00pCiD8LuVyOYZi+vj673W4wGMxms8fj2d/fV3DRarVD
Q0OVHfczhC0uLlIUheuYTCYvLy/j8bjFYgEAhNDh4aGkF8/zADA2NlbZoUp37Pz8HCFktVqVe35/
fx+Px9PpNEEQAwMD3d3dbwg6na6rq+vo6AgASJK0Wq1WqxUbBUGIRqNNTU3lYW9vbwHAaDSqnb03
kJTLsqzb7cZF7e/vL5VKcoXZ2NgwGo00Tff09AAAQRCSHWBZFh/HMMw/RSVJAAgGg5KRs9ksACwv
L3+wVd8gIYxlWYPBgPMLBAIAkM1mJZ0zmQxCyOFwiKKYz+dx6qurq+VMQRAQQgDg8/mwhed5LEzu
miUSCQCIxWKVCZPYiiMjI62trXg8WlpaAADnVI5oNIpbCgAcx2Gjw+EoZ2o0GmzHrXt6egqHw6VS
aXh4uL29XTL4/z+KLMsKgoDf/X5/Y2OjXFUuLi4KhQJ+D4VCAOByueTINE0DAEEQDMNUVVW5XK6V
lRWFkjMMAwC5XE5Vg8qgtBWPj48RQolE4t0o19fXer0eAFKplBwnEongUqbTaTWZTUxMAMDd3d2r
5bXcaiArTBAEt9sdCATURPH5fABA07QCJ5PJYGELCwtqYtI0TZLkvy1er1eNI4bsug+FQiRJzs3N
vTvMW1tb0Wi0vr5+fn5egUZRFEmSpVLpdUMqo1AoEASxs7Oj1+s5jtve3n58fFTj+A2ScpeWlmw2
2+v9UcDV1ZXJZEIIHRwciKKYTCY3NzflyHh/UBT1bliv12symWw2G0VRbW1tHo9ncHDwQxtSQlgs
FjObzfl8Hn+Gw2EF/87OTgCIRCL4MxgMrq2tSTJ5nnc6nbiaFotldnZWfZYV4O0o7u7u+v3+9fV1
hNDJyUkqlXp5eZHr9uTk5N7ent1uLxaLo6OjZ2dniUQimUxKksfHx81m89TUlNPpbG5urqur+8Bc
fRxfxO//oKurq4vFok6n02q1+DkzM9Pb21vu+fDwUFtbW1NTU/s9KIrSaDQ/NGk1eCvs0+A3/R/7
7/gr7E/DpxX2FTYEEai3ZoiBAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Now-we-illustrate-how-to-process-an-image-generated_captcha_images/222X.png">Now we illustrate how to process an image <code>generated_captcha_images/222X.png</code><a class="anchor-link" href="#Now-we-illustrate-how-to-process-an-image-generated_captcha_images/222X.png">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">matplotlib</span> inline
<span class="c1">#The line above is necesary to show Matplotlib&#39;s plots inside a Jupyter Notebook</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="k">import</span> <span class="n">pyplot</span> <span class="k">as</span> <span class="n">plt</span>
<span class="kn">import</span> <span class="nn">cv2</span> <span class="c1"># OpenCV, a popular framework for computer vision and image processing</span>

<span class="n">captcha_image_file</span> <span class="o">=</span> <span class="s1">&#39;generated_captcha_images/222X.png&#39;</span> <span class="c1"># normal</span>
<span class="c1"># captcha_image_file = &#39;generated_captcha_images/2W4M.png&#39; # try this: 3 objects, 2 letters are merged</span>
<span class="c1"># captcha_image_file = &#39;generated_captcha_images/3PH3.png&#39; # try this: 5 objects detected</span>
<span class="c1"># captcha_image_file = &#39;generated_captcha_images/JYU4.png&#39; # try this: 6 objects detected</span>

<span class="n">captcha_correct_text</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">captcha_image_file</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1"># Loading the image and convert it to grayscale</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">captcha_image_file</span><span class="p">)</span>
<span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2GRAY</span><span class="p">)</span>

<span class="c1">#Showing the image with matplotlib</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">gray</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
gg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Adding some extra padding around the image</span>
<span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">copyMakeBorder</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">BORDER_REPLICATE</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">gray</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># threshold the image (convert it to pure black and white)</span>
<span class="c1"># we use Otsu’s binarization</span>
<span class="c1"># check: https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html</span>
<span class="n">thresh</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">threshold</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_BINARY_INV</span> <span class="o">|</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_OTSU</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">thresh</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
oEtSI/4XPr3VcIZ+L3kAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># find the contours (continuous blobs of pixels) the image</span>
<span class="c1"># check:</span>
<span class="c1"># https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started</span>
<span class="n">contours</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">findContours</span><span class="p">(</span><span class="n">thresh</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="n">cv2</span><span class="o">.</span><span class="n">RETR_EXTERNAL</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">CHAIN_APPROX_SIMPLE</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>

<span class="n">zero_img</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros_like</span><span class="p">(</span><span class="n">thresh</span><span class="p">)</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">contours</span><span class="p">)):</span>
    <span class="n">temp</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">drawContours</span><span class="p">(</span><span class="n">zero_img</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="n">contours</span><span class="p">,</span> <span class="n">i</span><span class="p">,</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXQAAAC7CAYAAAB1qmWGAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo
dHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAC31JREFUeJzt3X+o3fV9x/Hna/nZpD9iVpU0kWkh
OMuYsQuazjE2rWtaRvWPDpQxMgjkn47pKGxxg4GwPyyMtvtjDMJ0DaNoO+umSKnLMkvZGNH4q42m
aWxrNTMzdtPZbSCme++P873r5fbee865P873+PH5gMM538/5Hr4vzvd7X/nez/mem1QVkqS3vp/q
O4AkaWVY6JLUCAtdkhphoUtSIyx0SWqEhS5JjbDQJakRFrokNWJZhZ5kb5JTSZ5LcnClQkmSxpel
flM0yRrg28ANwBngMeCWqnp25eJJkka1dhmvvRp4rqq+C5DkXuBGYMFCX58NtZHNy9ikJL39/JBX
f1BVFw5bbzmFvh14cdbyGeCaxV6wkc1ck+uXsUlJevv5h7rv+6Ost5xCzzxjPzF/k+QAcABgI5uW
sTlJ0mKW86HoGeCSWcs7gJfmrlRVh6pqd1XtXseGZWxOkrSY5RT6Y8DOJJclWQ/cDDy4MrEkSeNa
8pRLVZ1P8jvAw8Aa4O6qembFkkmSxrKcOXSq6ivAV1YoiyRpGfymqCQ1wkKXpEZY6JLUCAtdkhph
oUtSIyx0SWqEhS5JjbDQJakRFrokNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUuSY2w0CWpERa6
JDXCQpekRljoktQIC12SGmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtS
I4YWepK7k5xLcmLW2NYkR5Kc7u4vWN2YkqRhRjlD/zywd87YQeBoVe0EjnbLkqQeDS30qvo68B9z
hm8EDnePDwM3rXAuSdKYljqHfnFVnQXo7i9auUiSpKVYu9obSHIAOACwkU2rvTlJetta6hn6y0m2
AXT35xZasaoOVdXuqtq9jg1L3JwkaZilFvqDwL7u8T7ggZWJI0laqlEuW7wH+Bfg8iRnkuwH7gRu
SHIauKFbliT1aOgcelXdssBT169wFknSMvhNUUlqhIUuSY2w0CWpERa6JDXCQpekRljoktQIC12S
GmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtSIyx0SWqEhS5JjbDQJakR
Q/9PUWmYh196asmv/cj7dq1gEuntzTN0SWqEhS5JjbDQJakRzqFrbMPmzOfOi89ef7Hn5nte0ug8
Q5ekRljoktQIC12SGuEcuoYad858seeXc826pMV5hi5JjRha6EkuSfJIkpNJnklyaze+NcmRJKe7
+wtWP64kaSGjTLmcBz5VVU8keRfweJIjwG8DR6vqziQHgYPAH6xeVPVlNS8l9DJFaeUMPUOvqrNV
9UT3+IfASWA7cCNwuFvtMHDTaoWUJA031hx6kkuBq4BjwMVVdRYGpQ9ctNLhJEmjG7nQk7wT+DJw
W1W9PsbrDiQ5nuT4m7yxlIySpBGMdNliknUMyvwLVXV/N/xykm1VdTbJNuDcfK+tqkPAIYB3Z2ut
QGa9xXipojQZo1zlEuAu4GRVfWbWUw8C+7rH+4AHVj6eJGlUo5yhXwv8FvDNJDOnWn8I3Al8Kcl+
4AXgN1YnoiRpFEMLvar+CcgCT1+/snEkSUvlV/+14habM/e6c2n1+NV/SWqEhS5JjbDQJakRzqFr
1TlvLk2GZ+iS1AgLXZIaYaFLUiOcQ9eyzb3u3DlzqR+eoUtSIyx0SWqEhS5JjXAOXWNzzlyaTp6h
S1IjLHRJaoRTLhpqJadYnK6RVo9n6JLUCAtdkhphoUtSI5xD17wW+2/kFntOUn88Q5ekRljoktQI
C12SGuEcuubl9eHSW49n6JLUCAtdkhphoUtSIyx0SWqEhS5JjRha6Ek2Jnk0ydNJnklyRzd+WZJj
SU4n+WKS9asfV5K0kFHO0N8ArquqK4FdwN4ke4BPA5+tqp3Aq8D+1YspSRpmaKHXwH91i+u6WwHX
Afd144eBm1YloSRpJCPNoSdZk+Qp4BxwBPgO8FpVne9WOQNsX52IkqRRjFToVfWjqtoF7ACuBq6Y
b7X5XpvkQJLjSY6/yRtLTypJWtRYV7lU1WvA14A9wJYkM386YAfw0gKvOVRVu6tq9zo2LCerJGkR
o1zlcmGSLd3jdwAfBk4CjwCf6FbbBzywWiElScON8se5tgGHk6xh8A/Al6rqoSTPAvcm+RPgSeCu
VcwpSRpiaKFX1TeAq+YZ/y6D+XRJ0hTwm6KS1AgLXZIaYaFLUiMsdElqhIUuSY2w0CWpERa6JDXC
QpekRljoktQIC12SGmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtSIyx0
SWqEhS5JjbDQJakRFrokNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUuSY2w0CWpERa6JDUiVTW5
jSWvAN8H3gv8YGIbHp25xmOu8ZhrPOb6sZ+pqguHrTTRQv//jSbHq2r3xDc8hLnGY67xmGs85hqf
Uy6S1AgLXZIa0VehH+ppu8OYazzmGo+5xmOuMfUyhy5JWnlOuUhSIyZa6En2JjmV5LkkBye57Xmy
3J3kXJITs8a2JjmS5HR3f8GEM12S5JEkJ5M8k+TWKcm1McmjSZ7uct3RjV+W5FiX64tJ1k8y16x8
a5I8meShacmV5Pkk30zyVJLj3Viv+7HLsCXJfUm+1R1nH5qSXJd379XM7fUkt/WdLcnvdcf8iST3
dD8LvR9fC5lYoSdZA/w58FHgA8AtST4wqe3P4/PA3jljB4GjVbUTONotT9J54FNVdQWwB/hk9x71
nesN4LqquhLYBexNsgf4NPDZLterwP4J55pxK3By1vK05PrVqto16xK3vvcjwJ8BX62qnwWuZPC+
9Z6rqk5179Uu4BeA/wH+ts9sSbYDvwvsrqqfA9YANzM9x9dPqqqJ3IAPAQ/PWr4duH1S218g06XA
iVnLp4Bt3eNtwKme8z0A3DBNuYBNwBPANQy+XLF2vv07wTw7GPygXwc8BGRKcj0PvHfOWK/7EXg3
8D26z86mJdc8OX8N+Oe+swHbgReBrcDa7vj6yDQcXwvdJjnlMvPmzDjTjU2Ti6vqLEB3f1FfQZJc
ClwFHJuGXN20xlPAOeAI8B3gtao6363S1/78HPD7wP92yz89JbkK+Pskjyc50I31vR/fD7wC/FU3
RfWXSTZPQa65bgbu6R73lq2q/hX4U+AF4Czwn8DjTMfxNa9JFnrmGfMSm3kkeSfwZeC2qnq97zwA
VfWjGvw6vAO4GrhivtUmmSnJrwPnqurx2cPzrNrHcXZtVX2QwRTjJ5P8cg8Z5loLfBD4i6q6Cvhv
+pn2WVA3H/1x4G+mIMsFwI3AZcD7gM0M9udcU9Njkyz0M8Als5Z3AC9NcPujeDnJNoDu/tykAyRZ
x6DMv1BV909LrhlV9RrwNQZz/FuSrO2e6mN/Xgt8PMnzwL0Mpl0+NwW5qKqXuvtzDOaCr6b//XgG
OFNVx7rl+xgUfN+5Zvso8ERVvdwt95ntw8D3quqVqnoTuB/4Rabg+FrIJAv9MWBn9wnxega/Vj04
we2P4kFgX/d4H4M57IlJEuAu4GRVfWaKcl2YZEv3+B0MDvSTwCPAJ/rKVVW3V9WOqrqUwfH0j1X1
m33nSrI5ybtmHjOYEz5Bz/uxqv4NeDHJ5d3Q9cCzfeea4xZ+PN0C/WZ7AdiTZFP3sznzfvV6fC1q
wh92fAz4NoP51z/q88MDBgfNWeBNBmcu+xnMvx4FTnf3Wyec6ZcY/Pr2DeCp7vaxKcj188CTXa4T
wB934+8HHgWeY/Ar8oYe9+evAA9NQ65u+093t2dmjvW+92OXYRdwvNuXfwdcMA25umybgH8H3jNr
rO9j/w7gW91x/9fAhr6Pr8VuflNUkhrhN0UlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtSIyx0SWqE
hS5Jjfg/eDtAQYYXzjgAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
NeL/AFt5aB3Vxl3AAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXQAAAC7CAYAAAB1qmWGAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo
dHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAC25JREFUeJzt3H+s3fVdx/Hny/5cu822DkjXEmEJ
QRYjZTbAxBiF4brFDP6YCcSYmjTpPzOCWaJFExMS/2CJ2eYfxqQRXGMW2GQoDVnEWlmMxhQKlK2l
68o2BrWVMgWZmhA63/5xvnXXu3vvOef+ON+zD89HcnLO93O+J99Xzvd7X/d7P+d7bqoKSdKPvh/r
O4AkaXlY6JLUCAtdkhphoUtSIyx0SWqEhS5JjbDQJakRFrokNWJJhZ5kV5JTSV5Ism+5QkmSxpfF
flM0ySrgG8CtwBngKeDOqnp++eJJkka1egmvvR54oaq+BZDkIeA2YN5CX5t1tZ6NS9ikJL39fI/X
vltVlwxbbymFvg14ecbyGeCGhV6wno3ckFuWsElJevv5u3r4O6Ost5RCzxxjPzR/k2QvsBdgPRuW
sDlJ0kKW8qHoGeDyGcvbgbOzV6qq/VW1s6p2rmHdEjYnSVrIUgr9KeCqJFcmWQvcARxcnliSpHEt
esqlqi4k+U3gcWAV8EBVnVi2ZJKksSxlDp2q+jLw5WXKIklaAr8pKkmNsNAlqREWuiQ1wkKXpEZY
6JLUCAtdkhphoUtSIyx0SWqEhS5JjbDQJakRFrokNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUu
SY2w0CWpERa6JDXCQpekRljoktQIC12SGmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLU
iKGFnuSBJOeTHJ8xtiXJoSSnu/vNKxtTkjTMKGfonwN2zRrbBxyuqquAw92yJKlHQwu9qv4B+PdZ
w7cBB7rHB4DblzmXJGlMi51Dv6yqzgF095cuXyRJ0mKsXukNJNkL7AVYz4aV3pwkvW0t9gz9lSRb
Abr78/OtWFX7q2pnVe1cw7pFbk6SNMxiC/0gsLt7vBt4dHniSJIWa5TLFh8E/hm4OsmZJHuA+4Bb
k5wGbu2WJUk9GjqHXlV3zvPULcucRZK0BCv+oaj+v8fPHht53Q+/d8cKJpHUGr/6L0mNsNAlqREW
uiQ1wjn0FTZ7znyhefHZ647zWknyDF2SGmGhS1IjLHRJaoRz6MtsnOvMJWk5eYYuSY2w0CWpEU65
LDMvLZTUF8/QJakRFrokNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUuSY2w0CWpERa6JDXCQpek
Rvi/XHq20L/b9f/CSBqHZ+iS1AgLXZIaYaFLUiOcQ58w58wlrRTP0CWpEUMLPcnlSZ5IcjLJiSR3
deNbkhxKcrq737zycSVJ8xllyuUC8MmqeibJu4CnkxwCfgM4XFX3JdkH7AN+d+Wi/mhaaIoFnGaR
tHyGnqFX1bmqeqZ7/D3gJLANuA040K12ALh9pUJKkoYbaw49yRXAdcAR4LKqOgeD0gcuXe5wkqTR
jVzoSd4JfAm4u6reGON1e5McTXL0Ld5cTEZJ0ghGumwxyRoGZf75qnqkG34lydaqOpdkK3B+rtdW
1X5gP8C7s6WWIfNUc85cUl9GucolwP3Ayar69IynDgK7u8e7gUeXP54kaVSjnKHfBPw68LUkF08/
fw+4D/hikj3AS8CvrkxESdIohhZ6Vf0jkHmevmV540iSFsuv/q+wpcyZz56Pd/5d0kL86r8kNcJC
l6RGWOiS1Ajn0Jdo2HXnw56XpOXiGbokNcJCl6RGWOiS1Ajn0JfIa8MlTQvP0CWpERa6JDXCQpek
RljoktQIC12SGmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtSIyx0SWqE
hS5JjbDQJakRFrokNcJCl6RGWOiS1IihhZ5kfZInkzyX5ESSe7vxK5McSXI6yReSrF35uJKk+Yxy
hv4mcHNVXQvsAHYluRH4FPCZqroKeA3Ys3IxJUnDDC30GvjPbnFNdyvgZuDhbvwAcPuKJJQkjWSk
OfQkq5IcA84Dh4BvAq9X1YVulTPAtpWJKEkaxUiFXlXfr6odwHbgeuCauVab67VJ9iY5muToW7y5
+KSSpAWNdZVLVb0OfAW4EdiUZHX31Hbg7Dyv2V9VO6tq5xrWLSWrJGkBo1zlckmSTd3jdwAfAk4C
TwAf71bbDTy6UiElScOtHr4KW4EDSVYx+AXwxap6LMnzwENJ/hB4Frh/BXNKkoYYWuhV9VXgujnG
v8VgPl2SNAX8pqgkNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUuSY2w0CWpERa6JDXCQpekRljo
ktQIC12SGmGhS1IjLHRJaoSFLkmNsNAlqREWuiQ1wkKXpEZY6JLUCAtdkhphoUtSIyx0SWqEhS5J
jbDQJakRFrokNcJCl6RGWOiS1AgLXZIaYaFLUiMsdElqhIUuSY1IVU1uY8mrwHeA9wDfndiGR2eu
8ZhrPOYaj7l+4Cer6pJhK0200P9vo8nRqto58Q0PYa7xmGs85hqPucbnlIskNcJCl6RG9FXo+3va
7jDmGo+5xmOu8ZhrTL3MoUuSlp9TLpLUiIkWepJdSU4leSHJvklue44sDyQ5n+T4jLEtSQ4lOd3d
b55wpsuTPJHkZJITSe6aklzrkzyZ5Lku173d+JVJjnS5vpBk7SRzzci3KsmzSR6bllxJXkzytSTH
khztxnrdj12GTUkeTvL17jj74JTkurp7ry7e3khyd9/Zkvx2d8wfT/Jg97PQ+/E1n4kVepJVwJ8A
HwHeD9yZ5P2T2v4cPgfsmjW2DzhcVVcBh7vlSboAfLKqrgFuBD7RvUd953oTuLmqrgV2ALuS3Ah8
CvhMl+s1YM+Ec110F3ByxvK05Pqlqtox4xK3vvcjwB8Df1NVPwVcy+B96z1XVZ3q3qsdwM8C/w38
VZ/ZkmwDfgvYWVU/DawC7mB6jq8fVlUTuQEfBB6fsXwPcM+ktj9PpiuA4zOWTwFbu8dbgVM953sU
uHWacgEbgGeAGxh8uWL1XPt3gnm2M/hBvxl4DMiU5HoReM+ssV73I/Bu4Nt0n51NS645cv4y8E99
ZwO2AS8DW4DV3fH14Wk4vua7TXLK5eKbc9GZbmyaXFZV5wC6+0v7CpLkCuA64Mg05OqmNY4B54FD
wDeB16vqQrdKX/vzs8DvAP/TLf/ElOQq4G+TPJ1kbzfW9358H/Aq8OfdFNWfJdk4BblmuwN4sHvc
W7aq+hfgj4CXgHPAfwBPMx3H15wmWeiZY8xLbOaQ5J3Al4C7q+qNvvMAVNX3a/Dn8HbgeuCauVab
ZKYkvwKcr6qnZw7PsWofx9lNVfUBBlOMn0jyCz1kmG018AHgT6vqOuC/6GfaZ17dfPTHgL+cgiyb
gduAK4H3AhsZ7M/ZpqbHJlnoZ4DLZyxvB85OcPujeCXJVoDu/vykAyRZw6DMP19Vj0xLrouq6nXg
Kwzm+DclWd091cf+vAn4WJIXgYcYTLt8dgpyUVVnu/vzDOaCr6f//XgGOFNVR7rlhxkUfN+5ZvoI
8ExVvdIt95ntQ8C3q+rVqnoLeAT4Oabg+JrPJAv9KeCq7hPitQz+rDo4we2P4iCwu3u8m8Ec9sQk
CXA/cLKqPj1FuS5Jsql7/A4GB/pJ4Ang433lqqp7qmp7VV3B4Hj6+6r6tb5zJdmY5F0XHzOYEz5O
z/uxqv4VeDnJ1d3QLcDzfeea5U5+MN0C/WZ7CbgxyYbuZ/Pi+9Xr8bWgCX/Y8VHgGwzmX3+/zw8P
GBw054C3GJy57GEw/3oYON3db5lwpp9n8OfbV4Fj3e2jU5DrZ4Bnu1zHgT/oxt8HPAm8wOBP5HU9
7s9fBB6bhlzd9p/rbicuHut978cuww7gaLcv/xrYPA25umwbgH8DfnzGWN/H/r3A17vj/i+AdX0f
Xwvd/KaoJDXCb4pKUiMsdElqhIUuSY2w0CWpERa6JDXCQpekRljoktQIC12SGvG/JF05HfeqN50A
AAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">contour</span> <span class="ow">in</span> <span class="n">contours</span><span class="p">:</span>
    <span class="c1"># Get the rectangle that contains the contour</span>
    <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">)</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">boundingRect</span><span class="p">(</span><span class="n">contour</span><span class="p">)</span>
    <span class="n">letter_image</span> <span class="o">=</span> <span class="n">gray</span><span class="p">[</span><span class="n">y</span><span class="p">:</span><span class="n">y</span><span class="o">+</span><span class="n">h</span><span class="p">,</span> <span class="n">x</span><span class="p">:</span><span class="n">x</span><span class="o">+</span><span class="n">w</span><span class="p">]</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">letter_image</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAO4AAAD8CAYAAABw8JiyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo
dHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAADc5JREFUeJzt3X2QVfV9x/HPxwUGgaQGUCu7KKho
ZDRWZycDkompJBOSOKJ5mOD4QG2nZlpNiGNisJ2WmSZ/2NFaM5OIcXxspJoM0cREE6VGJnXGYGCl
BiQqDwZWUFZt1WArT9/+sdeZLbIP7u/sufdb368ZZnfvnvO9n4H9cO69e8/5OSIEIJdDmh0AwLtH
cYGEKC6QEMUFEqK4QEIUF0iI4gIJUVwgIYoLJDSqzjubPLEtpk0dXTRjXc/hRfuPeX1/0f6StH9M
+f93+yv4m993aNn+pxzWU5xhd+wrnvH8WxOLZ4wbtado/wmH/E9xhgmH7C2e8R9P7Xk5Igb9Ia+1
uNOmjtYTD00tmnHSTX9dtP/Uf9tVtL8k7WofWzzjzSPaime8NrOsNE+c973iDN17/1A845Lnzi+e
cfrEbUX7z56wsTjDmWN3Fs+Y3LH990PZjofKQEIUF0iI4gIJFRXX9jzbz9jeaHtxVaEADGzYxbXd
Jum7kj4laaak823PrCoYgP6VHHE/LGljRGyOiN2S7pE0v5pYAAZSUtx2SX1fg+9u3AZghJUU1we5
7R3XwbF9qe3Vtlf3vFL+y3oAZcXtltT33RQdkrYfuFFE3BwRnRHRefik8jcdACgr7m8kzbA93fYY
SQsk3V9NLAADGfZbHiNir+3LJT0kqU3SbRGxvrJkAPpV9F7liHhQ0oMVZQEwRLxzCkiI4gIJUVwg
oVrPx63CdRffVrT/khcuKc4w6dbHi2dMmPWh4hm7z2r+78VXv/XH5UOWTCoesfaxsvNx1+r44gxL
DzmxeIb0gyFtxREXSIjiAglRXCAhigskRHGBhCgukBDFBRKiuEBCFBdIiOICCVFcICGKCyREcYGE
KC6QEMUFEqK4QEKOeMc1zEdM56ljo3Rh61Jb9pQvxHzZ3IuKZ3jf/uIZ/7zyX4v2P2H0+OIMVfjL
bXOKZ2ydXbai/Ka7TinOsGLOd4pnHH/0i2sionOw7TjiAglRXCAhigskRHGBhEoWtp5q+1HbG2yv
t72oymAA+ldyeda9kq6MiC7b75O0xvaKiHi6omwA+jHsI25E7IiIrsbnb0jaIBa2BmpRyXNc29Mk
nSZp1UG+x8LWQMWKi2t7gqQfSfpqRLx+4PdZ2BqoXlFxbY9Wb2mXRcS91UQCMJiSV5Ut6VZJGyLi
+uoiARhMyRF3jqSLJJ1le23jz6crygVgAMP+dVBEPCbJFWYBMES8cwpIiOICCaVb2LrU9NETime8
eP2Y4hmHn/NM8YzP3vj1ov3XLbqxOMMDb44tnrF9weTiGRv/6aii/Td97KbiDFL5z9ZQccQFEqK4
QEIUF0iI4gIJUVwgIYoLJERxgYQoLpAQxQUSorhAQhQXSIjiAglRXCAhigskRHGBhCgukNB77kT6
KnR1/qB4xkc+96XiGe3XvuP68+/KuZ/+ZHGGXX8/pXjGf55VfjL+pi8uLZ6RCUdcICGKCyREcYGE
KC6QUBWLfrXZftL2z6oIBGBwVRxxF6l3bVwANSldra9D0mck3VJNHABDUXrEvUHSVZL2V5AFwBCV
LLN5tqSdEbFmkO1YkR6oWOkym+fYfl7SPepdbvOuAzdiRXqgesMubkRcHREdETFN0gJJv4yICytL
BqBf/B4XSKiSkwwiYqWklVXMAjA4jrhAQhQXSIjiAglxIn2TXPytnxbPuO+Bo4v2/+8/fbk4g84o
Wwlekn685NryHDWuBt8KOOICCVFcICGKCyREcYGEKC6QEMUFEqK4QEIUF0iI4gIJUVwgIYoLJERx
gYQoLpAQxQUSorhAQhQXSIgT6Zvk0j/aXjzjh7PnFe3f9mhXcYZNl5b/398x6r11EnwVOOICCVFc
ICGKCyRUuszmYbaX2/6d7Q22Z1cVDED/Sl+c+rakX0TE522PkTSugkwABjHs4tp+v6SPSvozSYqI
3ZJ2VxMLwEBKHiofK6lH0u22n7R9i+3xFeUCMICS4o6SdLqkpRFxmqRdkhYfuBELWwPVKylut6Tu
iFjV+Hq5eov8f7CwNVC9koWtX5S0zfaJjZvmSnq6klQABlT6qvKXJS1rvKK8WdIl5ZEADKaouBGx
VlJnRVkADBHvnAISorhAQhQXSIjzcZvkhH/5q+IZMzZ3lw04ZmpxhpP+rqd4xrNn7iqeccLo99Z7
fzjiAglRXCAhigskRHGBhCgukBDFBRKiuEBCFBdIiOICCVFcICGKCyREcYGEKC6QEMUFEqK4QEIU
F0iIE+mHYdbazxfPOO6bTxXPOGZl2QXm/7372OIMU84rvyLved/7evGM9ZffWDwjE464QEIUF0iI
4gIJUVwgodIV6a+wvd72Ott32x5bVTAA/Rt2cW23S/qKpM6IOFlSm6QFVQUD0L/Sh8qjJB1qe5Sk
cZK2l0cCMJiSZTZfkHSdpK2Sdkh6LSIerioYgP6VPFT+gKT5kqZLmiJpvO0LD7IdK9IDFSt5qPxx
SVsioici9ki6V9IZB27EivRA9UqKu1XSLNvjbFu9K9JvqCYWgIGUPMddJWm5pC5Jv23MurmiXAAG
ULoi/RJJSyrKAmCIeOcUkBDFBRKiuEBC77kT6a999bjiGRMveKV4xpY7yk9i/3n798sGtP+6OMNH
Pvel4hkd16wqnvGNL/xJ0f7/eOTa4gx14ogLJERxgYQoLpAQxQUSorhAQhQXSIjiAglRXCAhigsk
RHGBhCgukBDFBRKiuEBCFBdIiOICCVFcIKFaT6Tfr9Bbsadoxjd7Ti/av+uCmUX7S9Lzl00qnrFh
zv+PFdQv/tZPi2fc98DRxTNWf63sRHp9nxPpAYwwigskRHGBhAYtru3bbO+0va7PbRNtr7D9XOPj
B0Y2JoC+hnLEvUPSvANuWyzpkYiYIemRxtcAajJocSPiV5JePeDm+ZLubHx+p6RzK84FYADDfY57
ZETskKTGxyOqiwRgMCP+4lTfha1fZmFroBLDLe5Lto+SpMbHnf1t2Hdh68ksbA1UYrjFvV/Swsbn
CyX9pJo4AIZiKL8OulvS45JOtN1t+y8kXSPpE7afk/SJxtcAajLoe5Uj4vx+vjW34iwAhoh3TgEJ
UVwgIYoLJOSIqO3Oxk+eGh+cf0XRjIm3P15RmuFrO2lG8Yw/3LC3eMavTrmveEapU5/o7yWQoWu/
anfxjH3Pbiraf8s1s4szPHbBdcUzjurYsSYiOgfbjiMukBDFBRKiuEBCFBdIiOICCVFcICGKCyRE
cYGEKC6QEMUFEqK4QEIUF0iI4gIJUVwgIYoLJERxgYRqXdj6+PaX9MA/lJ1svPLqKUX7r3rjuKL9
Janr1fITv7/Y3lU8oxXse7x8vbfXTym/UP64yROK9p+xtLs4wxmjryyeIX1tSFtxxAUSorhAQhQX
SIjiAgkNd0X6a23/zvZTtu+zfdjIxgTQ13BXpF8h6eSI+JCkZyVdXXEuAAMY1or0EfFwRLx9YeBf
S+oYgWwA+lHFc9w/l/Tz/r7Zd2HrV17ZX8HdASgqru2/lbRX0rL+tum7sPWkSbwWBlRh2O+csr1Q
0tmS5kad65gAGF5xbc+T9A1JZ0bEm9VGAjCY4a5I/x1J75O0wvZa2zeNcE4AfQx3RfpbRyALgCHi
1SIgIYoLJERxgYRqXZHedo+k3w+wyWRJL9cUZyCtkKMVMkitkaMVMkj15DgmIg4fbKNaizsY26sj
opMcrZGhVXK0QoZWyiHxUBlIieICCbVacW9udoCGVsjRChmk1sjRChmk1snRWs9xAQxNqx1xAQxB
yxTX9jzbz9jeaHtxE+5/qu1HbW+wvd72orozHJCnzfaTtn/WpPs/zPbyxiWKNtie3aQcVzT+PdbZ
vtv22Bru82CXa5poe4Xt5xofyy8oXaAlimu7TdJ3JX1K0kxJ59ueWXOMvZKujIiTJM2SdFkTMvS1
SNKGJt7/tyX9IiI+KOnUZmSx3S7pK5I6I+JkSW2SFtRw13fonZdrWizpkYiYIemRxtdN0xLFlfRh
SRsjYnNE7JZ0j6T5dQaIiB0R0dX4/A31/qC215nhbbY7JH1G0i1Nuv/3S/qoGieTRMTuiPivZmRR
74kwh9oeJWmcpO0jfYcHu1yTen8e72x8fqekc0c6x0Bapbjtkrb1+bpbTSqNJNmeJuk0SauaFOEG
SVdJata1fo6V1CPp9sbD9Vtsj687RES8IOk6SVsl7ZD0WkQ8XHeOhiMjYkcj1w5JRzQph6TWKa4P
cltTXu62PUHSjyR9NSJeb8L9ny1pZ0Ssqfu++xgl6XRJSyPiNEm71ISHho3nkfMlTZc0RdJ42xfW
naMVtUpxuyVN7fN1h2p4SHQg26PVW9plEXFv3fffMEfSObafV+9ThrNs31Vzhm5J3RHx9iOO5eot
ct0+LmlLRPRExB5J90o6owk5JOkl20dJUuPjziblkNQ6xf2NpBm2p9seo94XIO6vM4Btq/c53YaI
uL7O++4rIq6OiI6ImKbev4dfRkStR5mIeFHSNtsnNm6aK+npOjM0bJU0y/a4xr/PXDXvBbv7JS1s
fL5Q0k+alENSzcts9ici9tq+XNJD6n3l8LaIWF9zjDmSLpL0W9trG7f9TUQ8WHOOVvFlScsa/5Fu
lnRJ3QEiYpXt5ZK61Puq/5Oq4d1Ljcs1fUzSZNvdkpZIukbSDxuXbtoq6QsjnWMgvHMKSKhVHioD
eBcoLpAQxQUSorhAQhQXSIjiAglRXCAhigsk9L+6Dmn9a4HRAwAAAABJRU5ErkJggg==
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Putting-things-together:-get-letters-from-images">Putting things together: get letters from images<a class="anchor-link" href="#Putting-things-together:-get-letters-from-images">&#182;</a></h3><p>Using what we have learnt above, write your code to save get the letters of all images. The letter-images are stored as 32 folders under folder <code>extracted_letter_images</code>.</p>
<p>For example, <code>extracted_letter_images/A</code> is a folder that saves all images of letter <code>A</code>. After you complete, each letter-folder should contain over 1000 letter-images.</p>
<p>Hint: (1) consider how to name different files in a letter-folder differently? (2) ingore those images with number of contours other than 4.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">glob</span>
<span class="kn">import</span> <span class="nn">imutils</span>
<span class="kn">import</span> <span class="nn">cv2</span>

<span class="n">LETTER_IMAGES_FOLDER</span> <span class="o">=</span> <span class="s2">&quot;extracted_letter_images&quot;</span> <span class="c1"># the output for training</span>
<span class="n">SKIPPED_FOLDER</span> <span class="o">=</span> <span class="s2">&quot;skipped_images&quot;</span> <span class="c1"># those images are skipped</span>
<span class="n">counts</span> <span class="o">=</span> <span class="p">{}</span> <span class="c1"># counts[&#39;A&#39;] = number of &#39;A&#39;-images, so that next &#39;A&#39;-image can be named as counts[&#39;A&#39;] + 1</span>

<span class="c1"># loop over the image paths</span>
<span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">captcha_image_file</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">captcha_image_files</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;[INFO] processing image </span><span class="si">{}</span><span class="s2">/</span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">captcha_image_files</span><span class="p">)))</span>

    <span class="c1"># getting file name</span>
    <span class="n">filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">captcha_image_file</span><span class="p">)</span>
    <span class="n">captcha_correct_text</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">filename</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

    <span class="c1"># Loading image and convert to grayscale</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">captcha_image_file</span><span class="p">)</span>
    <span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2GRAY</span><span class="p">)</span>

    <span class="c1"># Adding extra padding around the image</span>
    <span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">copyMakeBorder</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">BORDER_REPLICATE</span><span class="p">)</span>

    <span class="c1"># threshold the image with otsu&#39;s binarization</span>
    <span class="n">thresh</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">threshold</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_BINARY_INV</span> <span class="o">|</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_OTSU</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>

    <span class="c1"># find the contours</span>
    <span class="n">contours</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">findContours</span><span class="p">(</span><span class="n">thresh</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="n">cv2</span><span class="o">.</span><span class="n">RETR_EXTERNAL</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">CHAIN_APPROX_SIMPLE</span><span class="p">)</span>
    <span class="n">contours</span> <span class="o">=</span> <span class="n">contours</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">imutils</span><span class="o">.</span><span class="n">is_cv2</span><span class="p">()</span> <span class="k">else</span> <span class="n">contours</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

    <span class="n">letter_image_regions</span> <span class="o">=</span> <span class="p">[]</span>

    
    <span class="k">for</span> <span class="n">contour</span> <span class="ow">in</span> <span class="n">contours</span><span class="p">:</span>
        <span class="c1"># Get the rectangle that contains the contour</span>
        <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">)</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">boundingRect</span><span class="p">(</span><span class="n">contour</span><span class="p">)</span>

        <span class="c1"># Compare countour width and height</span>
        <span class="k">if</span> <span class="n">w</span> <span class="o">/</span> <span class="n">h</span> <span class="o">&gt;</span> <span class="mf">1.25</span><span class="p">:</span>
            <span class="n">half_width</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">w</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
            <span class="n">letter_image_regions</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">half_width</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span>
            <span class="n">letter_image_regions</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span> <span class="o">+</span> <span class="n">half_width</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">half_width</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">letter_image_regions</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span>

    <span class="c1"># If we found more or less than 4 letters in the captcha, save to skipped</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">4</span><span class="p">:</span>
        <span class="n">cv2</span><span class="o">.</span><span class="n">imwrite</span><span class="p">(</span><span class="n">SKIPPED_FOLDER</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span> <span class="o">+</span> <span class="n">captcha_correct_text</span> <span class="o">+</span> <span class="s2">&quot;.png&quot;</span><span class="p">,</span> <span class="n">image</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">letter_image_regions</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>

    <span class="c1">#give each letter a single image</span>
    <span class="k">for</span> <span class="n">letter_bounding_box</span><span class="p">,</span> <span class="n">letter_text</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">,</span> <span class="n">captcha_correct_text</span><span class="p">):</span>
        
        <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="n">letter_bounding_box</span>
        <span class="n">letter_image</span> <span class="o">=</span> <span class="n">gray</span><span class="p">[</span><span class="n">y</span> <span class="o">-</span> <span class="mi">2</span><span class="p">:</span><span class="n">y</span> <span class="o">+</span> <span class="n">h</span> <span class="o">+</span> <span class="mi">2</span><span class="p">,</span> <span class="n">x</span> <span class="o">-</span> <span class="mi">2</span><span class="p">:</span><span class="n">x</span> <span class="o">+</span> <span class="n">w</span> <span class="o">+</span> <span class="mi">2</span><span class="p">]</span>

        <span class="c1">#saving image</span>
        <span class="n">save_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">LETTER_IMAGES_FOLDER</span><span class="p">,</span> <span class="n">letter_text</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">save_path</span><span class="p">):</span>
            <span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">save_path</span><span class="p">)</span>

        <span class="c1">#image to file</span>
        <span class="n">count</span> <span class="o">=</span> <span class="n">counts</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">letter_text</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
        <span class="n">p</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">save_path</span><span class="p">,</span> <span class="s2">&quot;</span><span class="si">{}</span><span class="s2">.png&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">count</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">6</span><span class="p">)))</span>
        <span class="n">cv2</span><span class="o">.</span><span class="n">imwrite</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">letter_image</span><span class="p">)</span>
        <span class="n">counts</span><span class="p">[</span><span class="n">letter_text</span><span class="p">]</span> <span class="o">=</span> <span class="n">count</span> <span class="o">+</span> <span class="mi">1</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[INFO] processing image 1/9955
[INFO] processing image 2/9955
[INFO] processing image 3/9955
[INFO] processing image 4/9955
[INFO] processing image 5/9955
[INFO] processing image 6/9955
[INFO] processing image 7/9955
[INFO] processing image 8/9955
[INFO] processing image 9/9955
[INFO] processing image 10/9955
[INFO] processing image 11/9955
[INFO] processing image 12/9955
[INFO] processing image 13/9955
[INFO] processing image 14/9955
[INFO] processing image 15/9955
[INFO] processing image 16/9955
[INFO] processing image 17/9955
[INFO] processing image 18/9955
[INFO] processing image 19/9955
[INFO] processing image 20/9955
[INFO] processing image 21/9955
[INFO] processing image 22/9955
[INFO] processing image 23/9955
[INFO] processing image 24/9955
[INFO] processing image 25/9955
[INFO] processing image 26/9955
[INFO] processing image 27/9955
[INFO] processing image 28/9955
[INFO] processing image 29/9955
[INFO] processing image 30/9955
[INFO] processing image 31/9955
[INFO] processing image 32/9955
[INFO] processing image 33/9955
[INFO] processing image 34/9955
[INFO] processing image 35/9955
[INFO] processing image 36/9955
[INFO] processing image 37/9955
[INFO] processing image 38/9955
[INFO] processing image 39/9955
[INFO] processing image 40/9955
[INFO] processing image 41/9955
[INFO] processing image 42/9955
[INFO] processing image 43/9955
[INFO] processing image 44/9955
[INFO] processing image 45/9955
[INFO] processing image 46/9955
[INFO] processing image 47/9955
[INFO] processing image 48/9955
[INFO] processing image 49/9955
[INFO] processing image 50/9955
[INFO] processing image 51/9955
[INFO] processing image 52/9955
[INFO] processing image 53/9955
[INFO] processing image 54/9955
[INFO] processing image 55/9955
[INFO] processing image 56/9955
[INFO] processing image 57/9955
[INFO] processing image 58/9955
[INFO] processing image 59/9955
[INFO] processing image 60/9955
[INFO] processing image 61/9955
[INFO] processing image 62/9955
[INFO] processing image 63/9955
[INFO] processing image 64/9955
[INFO] processing image 65/9955
[INFO] processing image 66/9955
[INFO] processing image 67/9955
[INFO] processing image 68/9955
[INFO] processing image 69/9955
[INFO] processing image 70/9955
[INFO] processing image 71/9955
[INFO] processing image 72/9955
[INFO] processing image 73/9955
[INFO] processing image 74/9955
[INFO] processing image 75/9955
[INFO] processing image 76/9955
[INFO] processing image 77/9955
[INFO] processing image 78/9955
[INFO] processing image 79/9955
[INFO] processing image 80/9955
[INFO] processing image 81/9955
[INFO] processing image 82/9955
[INFO] processing image 83/9955
[INFO] processing image 84/9955
[INFO] processing image 85/9955
[INFO] processing image 86/9955
[INFO] processing image 87/9955
[INFO] processing image 88/9955
[INFO] processing image 89/9955
[INFO] processing image 90/9955
[INFO] processing image 91/9955
[INFO] processing image 92/9955
[INFO] processing image 93/9955
[INFO] processing image 94/9955
[INFO] processing image 95/9955
[INFO] processing image 96/9955
[INFO] processing image 97/9955
[INFO] processing image 98/9955
[INFO] processing image 99/9955
[INFO] processing image 100/9955
[INFO] processing image 101/9955
[INFO] processing image 102/9955
[INFO] processing image 103/9955
[INFO] processing image 104/9955
[INFO] processing image 105/9955
[INFO] processing image 106/9955
[INFO] processing image 107/9955
[INFO] processing image 108/9955
[INFO] processing image 109/9955
[INFO] processing image 110/9955
[INFO] processing image 111/9955
[INFO] processing image 112/9955
[INFO] processing image 113/9955
[INFO] processing image 114/9955
[INFO] processing image 115/9955
[INFO] processing image 116/9955
[INFO] processing image 117/9955
[INFO] processing image 118/9955
[INFO] processing image 119/9955
[INFO] processing image 120/9955
[INFO] processing image 121/9955
[INFO] processing image 122/9955
[INFO] processing image 123/9955
[INFO] processing image 124/9955
[INFO] processing image 125/9955
[INFO] processing image 126/9955
[INFO] processing image 127/9955
[INFO] processing image 128/9955
[INFO] processing image 129/9955
[INFO] processing image 130/9955
[INFO] processing image 131/9955
[INFO] processing image 132/9955
[INFO] processing image 133/9955
[INFO] processing image 134/9955
[INFO] processing image 135/9955
[INFO] processing image 136/9955
[INFO] processing image 137/9955
[INFO] processing image 138/9955
[INFO] processing image 139/9955
[INFO] processing image 140/9955
[INFO] processing image 141/9955
[INFO] processing image 142/9955
[INFO] processing image 143/9955
[INFO] processing image 144/9955
[INFO] processing image 145/9955
[INFO] processing image 146/9955
[INFO] processing image 147/9955
[INFO] processing image 148/9955
[INFO] processing image 149/9955
[INFO] processing image 150/9955
[INFO] processing image 151/9955
[INFO] processing image 152/9955
[INFO] processing image 153/9955
[INFO] processing image 154/9955
[INFO] processing image 155/9955
[INFO] processing image 156/9955
[INFO] processing image 157/9955
[INFO] processing image 158/9955
[INFO] processing image 159/9955
[INFO] processing image 160/9955
[INFO] processing image 161/9955
[INFO] processing image 162/9955
[INFO] processing image 163/9955
[INFO] processing image 164/9955
[INFO] processing image 165/9955
[INFO] processing image 166/9955
[INFO] processing image 167/9955
[INFO] processing image 168/9955
[INFO] processing image 169/9955
[INFO] processing image 170/9955
[INFO] processing image 171/9955
[INFO] processing image 172/9955
[INFO] processing image 173/9955
[INFO] processing image 174/9955
[INFO] processing image 175/9955
[INFO] processing image 176/9955
[INFO] processing image 177/9955
[INFO] processing image 178/9955
[INFO] processing image 179/9955
[INFO] processing image 180/9955
[INFO] processing image 181/9955
[INFO] processing image 182/9955
[INFO] processing image 183/9955
[INFO] processing image 184/9955
[INFO] processing image 185/9955
[INFO] processing image 186/9955
[INFO] processing image 187/9955
[INFO] processing image 188/9955
[INFO] processing image 189/9955
[INFO] processing image 190/9955
[INFO] processing image 191/9955
[INFO] processing image 192/9955
[INFO] processing image 193/9955
[INFO] processing image 194/9955
[INFO] processing image 195/9955
[INFO] processing image 196/9955
[INFO] processing image 197/9955
[INFO] processing image 198/9955
[INFO] processing image 199/9955
[INFO] processing image 200/9955
[INFO] processing image 201/9955
[INFO] processing image 202/9955
[INFO] processing image 203/9955
[INFO] processing image 204/9955
[INFO] processing image 205/9955
[INFO] processing image 206/9955
[INFO] processing image 207/9955
[INFO] processing image 208/9955
[INFO] processing image 209/9955
[INFO] processing image 210/9955
[INFO] processing image 211/9955
[INFO] processing image 212/9955
[INFO] processing image 213/9955
[INFO] processing image 214/9955
[INFO] processing image 215/9955
[INFO] processing image 216/9955
[INFO] processing image 217/9955
[INFO] processing image 218/9955
[INFO] processing image 219/9955
[INFO] processing image 220/9955
[INFO] processing image 221/9955
[INFO] processing image 222/9955
[INFO] processing image 223/9955
[INFO] processing image 224/9955
[INFO] processing image 225/9955
[INFO] processing image 226/9955
[INFO] processing image 227/9955
[INFO] processing image 228/9955
[INFO] processing image 229/9955
[INFO] processing image 230/9955
[INFO] processing image 231/9955
[INFO] processing image 232/9955
[INFO] processing image 233/9955
[INFO] processing image 234/9955
[INFO] processing image 235/9955
[INFO] processing image 236/9955
[INFO] processing image 237/9955
[INFO] processing image 238/9955
[INFO] processing image 239/9955
[INFO] processing image 240/9955
[INFO] processing image 241/9955
[INFO] processing image 242/9955
[INFO] processing image 243/9955
[INFO] processing image 244/9955
[INFO] processing image 245/9955
[INFO] processing image 246/9955
[INFO] processing image 247/9955
[INFO] processing image 248/9955
[INFO] processing image 249/9955
[INFO] processing image 250/9955
[INFO] processing image 251/9955
[INFO] processing image 252/9955
[INFO] processing image 253/9955
[INFO] processing image 254/9955
[INFO] processing image 255/9955
[INFO] processing image 256/9955
[INFO] processing image 257/9955
[INFO] processing image 258/9955
[INFO] processing image 259/9955
[INFO] processing image 260/9955
[INFO] processing image 261/9955
[INFO] processing image 262/9955
[INFO] processing image 263/9955
[INFO] processing image 264/9955
[INFO] processing image 265/9955
[INFO] processing image 266/9955
[INFO] processing image 267/9955
[INFO] processing image 268/9955
[INFO] processing image 269/9955
[INFO] processing image 270/9955
[INFO] processing image 271/9955
[INFO] processing image 272/9955
[INFO] processing image 273/9955
[INFO] processing image 274/9955
[INFO] processing image 275/9955
[INFO] processing image 276/9955
[INFO] processing image 277/9955
[INFO] processing image 278/9955
[INFO] processing image 279/9955
[INFO] processing image 280/9955
[INFO] processing image 281/9955
[INFO] processing image 282/9955
[INFO] processing image 283/9955
[INFO] processing image 284/9955
[INFO] processing image 285/9955
[INFO] processing image 286/9955
[INFO] processing image 287/9955
[INFO] processing image 288/9955
[INFO] processing image 289/9955
[INFO] processing image 290/9955
[INFO] processing image 291/9955
[INFO] processing image 292/9955
[INFO] processing image 293/9955
[INFO] processing image 294/9955
[INFO] processing image 295/9955
[INFO] processing image 296/9955
[INFO] processing image 297/9955
[INFO] processing image 298/9955
[INFO] processing image 299/9955
[INFO] processing image 300/9955
[INFO] processing image 301/9955
[INFO] processing image 302/9955
[INFO] processing image 303/9955
[INFO] processing image 304/9955
[INFO] processing image 305/9955
[INFO] processing image 306/9955
[INFO] processing image 307/9955
[INFO] processing image 308/9955
[INFO] processing image 309/9955
[INFO] processing image 310/9955
[INFO] processing image 311/9955
[INFO] processing image 312/9955
[INFO] processing image 313/9955
[INFO] processing image 314/9955
[INFO] processing image 315/9955
[INFO] processing image 316/9955
[INFO] processing image 317/9955
[INFO] processing image 318/9955
[INFO] processing image 319/9955
[INFO] processing image 320/9955
[INFO] processing image 321/9955
[INFO] processing image 322/9955
[INFO] processing image 323/9955
[INFO] processing image 324/9955
[INFO] processing image 325/9955
[INFO] processing image 326/9955
[INFO] processing image 327/9955
[INFO] processing image 328/9955
[INFO] processing image 329/9955
[INFO] processing image 330/9955
[INFO] processing image 331/9955
[INFO] processing image 332/9955
[INFO] processing image 333/9955
[INFO] processing image 334/9955
[INFO] processing image 335/9955
[INFO] processing image 336/9955
[INFO] processing image 337/9955
[INFO] processing image 338/9955
[INFO] processing image 339/9955
[INFO] processing image 340/9955
[INFO] processing image 341/9955
[INFO] processing image 342/9955
[INFO] processing image 343/9955
[INFO] processing image 344/9955
[INFO] processing image 345/9955
[INFO] processing image 346/9955
[INFO] processing image 347/9955
[INFO] processing image 348/9955
[INFO] processing image 349/9955
[INFO] processing image 350/9955
[INFO] processing image 351/9955
[INFO] processing image 352/9955
[INFO] processing image 353/9955
[INFO] processing image 354/9955
[INFO] processing image 355/9955
[INFO] processing image 356/9955
[INFO] processing image 357/9955
[INFO] processing image 358/9955
[INFO] processing image 359/9955
[INFO] processing image 360/9955
[INFO] processing image 361/9955
[INFO] processing image 362/9955
[INFO] processing image 363/9955
[INFO] processing image 364/9955
[INFO] processing image 365/9955
[INFO] processing image 366/9955
[INFO] processing image 367/9955
[INFO] processing image 368/9955
[INFO] processing image 369/9955
[INFO] processing image 370/9955
[INFO] processing image 371/9955
[INFO] processing image 372/9955
[INFO] processing image 373/9955
[INFO] processing image 374/9955
[INFO] processing image 375/9955
[INFO] processing image 376/9955
[INFO] processing image 377/9955
[INFO] processing image 378/9955
[INFO] processing image 379/9955
[INFO] processing image 380/9955
[INFO] processing image 381/9955
[INFO] processing image 382/9955
[INFO] processing image 383/9955
[INFO] processing image 384/9955
[INFO] processing image 385/9955
[INFO] processing image 386/9955
[INFO] processing image 387/9955
[INFO] processing image 388/9955
[INFO] processing image 389/9955
[INFO] processing image 390/9955
[INFO] processing image 391/9955
[INFO] processing image 392/9955
[INFO] processing image 393/9955
[INFO] processing image 394/9955
[INFO] processing image 395/9955
[INFO] processing image 396/9955
[INFO] processing image 397/9955
[INFO] processing image 398/9955
[INFO] processing image 399/9955
[INFO] processing image 400/9955
[INFO] processing image 401/9955
[INFO] processing image 402/9955
[INFO] processing image 403/9955
[INFO] processing image 404/9955
[INFO] processing image 405/9955
[INFO] processing image 406/9955
[INFO] processing image 407/9955
[INFO] processing image 408/9955
[INFO] processing image 409/9955
[INFO] processing image 410/9955
[INFO] processing image 411/9955
[INFO] processing image 412/9955
[INFO] processing image 413/9955
[INFO] processing image 414/9955
[INFO] processing image 415/9955
[INFO] processing image 416/9955
[INFO] processing image 417/9955
[INFO] processing image 418/9955
[INFO] processing image 419/9955
[INFO] processing image 420/9955
[INFO] processing image 421/9955
[INFO] processing image 422/9955
[INFO] processing image 423/9955
[INFO] processing image 424/9955
[INFO] processing image 425/9955
[INFO] processing image 426/9955
[INFO] processing image 427/9955
[INFO] processing image 428/9955
[INFO] processing image 429/9955
[INFO] processing image 430/9955
[INFO] processing image 431/9955
[INFO] processing image 432/9955
[INFO] processing image 433/9955
[INFO] processing image 434/9955
[INFO] processing image 435/9955
[INFO] processing image 436/9955
[INFO] processing image 437/9955
[INFO] processing image 438/9955
[INFO] processing image 439/9955
[INFO] processing image 440/9955
[INFO] processing image 441/9955
[INFO] processing image 442/9955
[INFO] processing image 443/9955
[INFO] processing image 444/9955
[INFO] processing image 445/9955
[INFO] processing image 446/9955
[INFO] processing image 447/9955
[INFO] processing image 448/9955
[INFO] processing image 449/9955
[INFO] processing image 450/9955
[INFO] processing image 451/9955
[INFO] processing image 452/9955
[INFO] processing image 453/9955
[INFO] processing image 454/9955
[INFO] processing image 455/9955
[INFO] processing image 456/9955
[INFO] processing image 457/9955
[INFO] processing image 458/9955
[INFO] processing image 459/9955
[INFO] processing image 460/9955
[INFO] processing image 461/9955
[INFO] processing image 462/9955
[INFO] processing image 463/9955
[INFO] processing image 464/9955
[INFO] processing image 465/9955
[INFO] processing image 466/9955
[INFO] processing image 467/9955
[INFO] processing image 468/9955
[INFO] processing image 469/9955
[INFO] processing image 470/9955
[INFO] processing image 471/9955
[INFO] processing image 472/9955
[INFO] processing image 473/9955
[INFO] processing image 474/9955
[INFO] processing image 475/9955
[INFO] processing image 476/9955
[INFO] processing image 477/9955
[INFO] processing image 478/9955
[INFO] processing image 479/9955
[INFO] processing image 480/9955
[INFO] processing image 481/9955
[INFO] processing image 482/9955
[INFO] processing image 483/9955
[INFO] processing image 484/9955
[INFO] processing image 485/9955
[INFO] processing image 486/9955
[INFO] processing image 487/9955
[INFO] processing image 488/9955
[INFO] processing image 489/9955
[INFO] processing image 490/9955
[INFO] processing image 491/9955
[INFO] processing image 492/9955
[INFO] processing image 493/9955
[INFO] processing image 494/9955
[INFO] processing image 495/9955
[INFO] processing image 496/9955
[INFO] processing image 497/9955
[INFO] processing image 498/9955
[INFO] processing image 499/9955
[INFO] processing image 500/9955
[INFO] processing image 501/9955
[INFO] processing image 502/9955
[INFO] processing image 503/9955
[INFO] processing image 504/9955
[INFO] processing image 505/9955
[INFO] processing image 506/9955
[INFO] processing image 507/9955
[INFO] processing image 508/9955
[INFO] processing image 509/9955
[INFO] processing image 510/9955
[INFO] processing image 511/9955
[INFO] processing image 512/9955
[INFO] processing image 513/9955
[INFO] processing image 514/9955
[INFO] processing image 515/9955
[INFO] processing image 516/9955
[INFO] processing image 517/9955
[INFO] processing image 518/9955
[INFO] processing image 519/9955
[INFO] processing image 520/9955
[INFO] processing image 521/9955
[INFO] processing image 522/9955
[INFO] processing image 523/9955
[INFO] processing image 524/9955
[INFO] processing image 525/9955
[INFO] processing image 526/9955
[INFO] processing image 527/9955
[INFO] processing image 528/9955
[INFO] processing image 529/9955
[INFO] processing image 530/9955
[INFO] processing image 531/9955
[INFO] processing image 532/9955
[INFO] processing image 533/9955
[INFO] processing image 534/9955
[INFO] processing image 535/9955
[INFO] processing image 536/9955
[INFO] processing image 537/9955
[INFO] processing image 538/9955
[INFO] processing image 539/9955
[INFO] processing image 540/9955
[INFO] processing image 541/9955
[INFO] processing image 542/9955
[INFO] processing image 543/9955
[INFO] processing image 544/9955
[INFO] processing image 545/9955
[INFO] processing image 546/9955
[INFO] processing image 547/9955
[INFO] processing image 548/9955
[INFO] processing image 549/9955
[INFO] processing image 550/9955
[INFO] processing image 551/9955
[INFO] processing image 552/9955
[INFO] processing image 553/9955
[INFO] processing image 554/9955
[INFO] processing image 555/9955
[INFO] processing image 556/9955
[INFO] processing image 557/9955
[INFO] processing image 558/9955
[INFO] processing image 559/9955
[INFO] processing image 560/9955
[INFO] processing image 561/9955
[INFO] processing image 562/9955
[INFO] processing image 563/9955
[INFO] processing image 564/9955
[INFO] processing image 565/9955
[INFO] processing image 566/9955
[INFO] processing image 567/9955
[INFO] processing image 568/9955
[INFO] processing image 569/9955
[INFO] processing image 570/9955
[INFO] processing image 571/9955
[INFO] processing image 572/9955
[INFO] processing image 573/9955
[INFO] processing image 574/9955
[INFO] processing image 575/9955
[INFO] processing image 576/9955
[INFO] processing image 577/9955
[INFO] processing image 578/9955
[INFO] processing image 579/9955
[INFO] processing image 580/9955
[INFO] processing image 581/9955
[INFO] processing image 582/9955
[INFO] processing image 583/9955
[INFO] processing image 584/9955
[INFO] processing image 585/9955
[INFO] processing image 586/9955
[INFO] processing image 587/9955
[INFO] processing image 588/9955
[INFO] processing image 589/9955
[INFO] processing image 590/9955
[INFO] processing image 591/9955
[INFO] processing image 592/9955
[INFO] processing image 593/9955
[INFO] processing image 594/9955
[INFO] processing image 595/9955
[INFO] processing image 596/9955
[INFO] processing image 597/9955
[INFO] processing image 598/9955
[INFO] processing image 599/9955
[INFO] processing image 600/9955
[INFO] processing image 601/9955
[INFO] processing image 602/9955
[INFO] processing image 603/9955
[INFO] processing image 604/9955
[INFO] processing image 605/9955
[INFO] processing image 606/9955
[INFO] processing image 607/9955
[INFO] processing image 608/9955
[INFO] processing image 609/9955
[INFO] processing image 610/9955
[INFO] processing image 611/9955
[INFO] processing image 612/9955
[INFO] processing image 613/9955
[INFO] processing image 614/9955
[INFO] processing image 615/9955
[INFO] processing image 616/9955
[INFO] processing image 617/9955
[INFO] processing image 618/9955
[INFO] processing image 619/9955
[INFO] processing image 620/9955
[INFO] processing image 621/9955
[INFO] processing image 622/9955
[INFO] processing image 623/9955
[INFO] processing image 624/9955
[INFO] processing image 625/9955
[INFO] processing image 626/9955
[INFO] processing image 627/9955
[INFO] processing image 628/9955
[INFO] processing image 629/9955
[INFO] processing image 630/9955
[INFO] processing image 631/9955
[INFO] processing image 632/9955
[INFO] processing image 633/9955
[INFO] processing image 634/9955
[INFO] processing image 635/9955
[INFO] processing image 636/9955
[INFO] processing image 637/9955
[INFO] processing image 638/9955
[INFO] processing image 639/9955
[INFO] processing image 640/9955
[INFO] processing image 641/9955
[INFO] processing image 642/9955
[INFO] processing image 643/9955
[INFO] processing image 644/9955
[INFO] processing image 645/9955
[INFO] processing image 646/9955
[INFO] processing image 647/9955
[INFO] processing image 648/9955
[INFO] processing image 649/9955
[INFO] processing image 650/9955
[INFO] processing image 651/9955
[INFO] processing image 652/9955
[INFO] processing image 653/9955
[INFO] processing image 654/9955
[INFO] processing image 655/9955
[INFO] processing image 656/9955
[INFO] processing image 657/9955
[INFO] processing image 658/9955
[INFO] processing image 659/9955
[INFO] processing image 660/9955
[INFO] processing image 661/9955
[INFO] processing image 662/9955
[INFO] processing image 663/9955
[INFO] processing image 664/9955
[INFO] processing image 665/9955
[INFO] processing image 666/9955
[INFO] processing image 667/9955
[INFO] processing image 668/9955
[INFO] processing image 669/9955
[INFO] processing image 670/9955
[INFO] processing image 671/9955
[INFO] processing image 672/9955
[INFO] processing image 673/9955
[INFO] processing image 674/9955
[INFO] processing image 675/9955
[INFO] processing image 676/9955
[INFO] processing image 677/9955
[INFO] processing image 678/9955
[INFO] processing image 679/9955
[INFO] processing image 680/9955
[INFO] processing image 681/9955
[INFO] processing image 682/9955
[INFO] processing image 683/9955
[INFO] processing image 684/9955
[INFO] processing image 685/9955
[INFO] processing image 686/9955
[INFO] processing image 687/9955
[INFO] processing image 688/9955
[INFO] processing image 689/9955
[INFO] processing image 690/9955
[INFO] processing image 691/9955
[INFO] processing image 692/9955
[INFO] processing image 693/9955
[INFO] processing image 694/9955
[INFO] processing image 695/9955
[INFO] processing image 696/9955
[INFO] processing image 697/9955
[INFO] processing image 698/9955
[INFO] processing image 699/9955
[INFO] processing image 700/9955
[INFO] processing image 701/9955
[INFO] processing image 702/9955
[INFO] processing image 703/9955
[INFO] processing image 704/9955
[INFO] processing image 705/9955
[INFO] processing image 706/9955
[INFO] processing image 707/9955
[INFO] processing image 708/9955
[INFO] processing image 709/9955
[INFO] processing image 710/9955
[INFO] processing image 711/9955
[INFO] processing image 712/9955
[INFO] processing image 713/9955
[INFO] processing image 714/9955
[INFO] processing image 715/9955
[INFO] processing image 716/9955
[INFO] processing image 717/9955
[INFO] processing image 718/9955
[INFO] processing image 719/9955
[INFO] processing image 720/9955
[INFO] processing image 721/9955
[INFO] processing image 722/9955
[INFO] processing image 723/9955
[INFO] processing image 724/9955
[INFO] processing image 725/9955
[INFO] processing image 726/9955
[INFO] processing image 727/9955
[INFO] processing image 728/9955
[INFO] processing image 729/9955
[INFO] processing image 730/9955
[INFO] processing image 731/9955
[INFO] processing image 732/9955
[INFO] processing image 733/9955
[INFO] processing image 734/9955
[INFO] processing image 735/9955
[INFO] processing image 736/9955
[INFO] processing image 737/9955
[INFO] processing image 738/9955
[INFO] processing image 739/9955
[INFO] processing image 740/9955
[INFO] processing image 741/9955
[INFO] processing image 742/9955
[INFO] processing image 743/9955
[INFO] processing image 744/9955
[INFO] processing image 745/9955
[INFO] processing image 746/9955
[INFO] processing image 747/9955
[INFO] processing image 748/9955
[INFO] processing image 749/9955
[INFO] processing image 750/9955
[INFO] processing image 751/9955
[INFO] processing image 752/9955
[INFO] processing image 753/9955
[INFO] processing image 754/9955
[INFO] processing image 755/9955
[INFO] processing image 756/9955
[INFO] processing image 757/9955
[INFO] processing image 758/9955
[INFO] processing image 759/9955
[INFO] processing image 760/9955
[INFO] processing image 761/9955
[INFO] processing image 762/9955
[INFO] processing image 763/9955
[INFO] processing image 764/9955
[INFO] processing image 765/9955
[INFO] processing image 766/9955
[INFO] processing image 767/9955
[INFO] processing image 768/9955
[INFO] processing image 769/9955
[INFO] processing image 770/9955
[INFO] processing image 771/9955
[INFO] processing image 772/9955
[INFO] processing image 773/9955
[INFO] processing image 774/9955
[INFO] processing image 775/9955
[INFO] processing image 776/9955
[INFO] processing image 777/9955
[INFO] processing image 778/9955
[INFO] processing image 779/9955
[INFO] processing image 780/9955
[INFO] processing image 781/9955
[INFO] processing image 782/9955
[INFO] processing image 783/9955
[INFO] processing image 784/9955
[INFO] processing image 785/9955
[INFO] processing image 786/9955
[INFO] processing image 787/9955
[INFO] processing image 788/9955
[INFO] processing image 789/9955
[INFO] processing image 790/9955
[INFO] processing image 791/9955
[INFO] processing image 792/9955
[INFO] processing image 793/9955
[INFO] processing image 794/9955
[INFO] processing image 795/9955
[INFO] processing image 796/9955
[INFO] processing image 797/9955
[INFO] processing image 798/9955
[INFO] processing image 799/9955
[INFO] processing image 800/9955
[INFO] processing image 801/9955
[INFO] processing image 802/9955
[INFO] processing image 803/9955
[INFO] processing image 804/9955
[INFO] processing image 805/9955
[INFO] processing image 806/9955
[INFO] processing image 807/9955
[INFO] processing image 808/9955
[INFO] processing image 809/9955
[INFO] processing image 810/9955
[INFO] processing image 811/9955
[INFO] processing image 812/9955
[INFO] processing image 813/9955
[INFO] processing image 814/9955
[INFO] processing image 815/9955
[INFO] processing image 816/9955
[INFO] processing image 817/9955
[INFO] processing image 818/9955
[INFO] processing image 819/9955
[INFO] processing image 820/9955
[INFO] processing image 821/9955
[INFO] processing image 822/9955
[INFO] processing image 823/9955
[INFO] processing image 824/9955
[INFO] processing image 825/9955
[INFO] processing image 826/9955
[INFO] processing image 827/9955
[INFO] processing image 828/9955
[INFO] processing image 829/9955
[INFO] processing image 830/9955
[INFO] processing image 831/9955
[INFO] processing image 832/9955
[INFO] processing image 833/9955
[INFO] processing image 834/9955
[INFO] processing image 835/9955
[INFO] processing image 836/9955
[INFO] processing image 837/9955
[INFO] processing image 838/9955
[INFO] processing image 839/9955
[INFO] processing image 840/9955
[INFO] processing image 841/9955
[INFO] processing image 842/9955
[INFO] processing image 843/9955
[INFO] processing image 844/9955
[INFO] processing image 845/9955
[INFO] processing image 846/9955
[INFO] processing image 847/9955
[INFO] processing image 848/9955
[INFO] processing image 849/9955
[INFO] processing image 850/9955
[INFO] processing image 851/9955
[INFO] processing image 852/9955
[INFO] processing image 853/9955
[INFO] processing image 854/9955
[INFO] processing image 855/9955
[INFO] processing image 856/9955
[INFO] processing image 857/9955
[INFO] processing image 858/9955
[INFO] processing image 859/9955
[INFO] processing image 860/9955
[INFO] processing image 861/9955
[INFO] processing image 862/9955
[INFO] processing image 863/9955
[INFO] processing image 864/9955
[INFO] processing image 865/9955
[INFO] processing image 866/9955
[INFO] processing image 867/9955
[INFO] processing image 868/9955
[INFO] processing image 869/9955
[INFO] processing image 870/9955
[INFO] processing image 871/9955
[INFO] processing image 872/9955
[INFO] processing image 873/9955
[INFO] processing image 874/9955
[INFO] processing image 875/9955
[INFO] processing image 876/9955
[INFO] processing image 877/9955
[INFO] processing image 878/9955
[INFO] processing image 879/9955
[INFO] processing image 880/9955
[INFO] processing image 881/9955
[INFO] processing image 882/9955
[INFO] processing image 883/9955
[INFO] processing image 884/9955
[INFO] processing image 885/9955
[INFO] processing image 886/9955
[INFO] processing image 887/9955
[INFO] processing image 888/9955
[INFO] processing image 889/9955
[INFO] processing image 890/9955
[INFO] processing image 891/9955
[INFO] processing image 892/9955
[INFO] processing image 893/9955
[INFO] processing image 894/9955
[INFO] processing image 895/9955
[INFO] processing image 896/9955
[INFO] processing image 897/9955
[INFO] processing image 898/9955
[INFO] processing image 899/9955
[INFO] processing image 900/9955
[INFO] processing image 901/9955
[INFO] processing image 902/9955
[INFO] processing image 903/9955
[INFO] processing image 904/9955
[INFO] processing image 905/9955
[INFO] processing image 906/9955
[INFO] processing image 907/9955
[INFO] processing image 908/9955
[INFO] processing image 909/9955
[INFO] processing image 910/9955
[INFO] processing image 911/9955
[INFO] processing image 912/9955
[INFO] processing image 913/9955
[INFO] processing image 914/9955
[INFO] processing image 915/9955
[INFO] processing image 916/9955
[INFO] processing image 917/9955
[INFO] processing image 918/9955
[INFO] processing image 919/9955
[INFO] processing image 920/9955
[INFO] processing image 921/9955
[INFO] processing image 922/9955
[INFO] processing image 923/9955
[INFO] processing image 924/9955
[INFO] processing image 925/9955
[INFO] processing image 926/9955
[INFO] processing image 927/9955
[INFO] processing image 928/9955
[INFO] processing image 929/9955
[INFO] processing image 930/9955
[INFO] processing image 931/9955
[INFO] processing image 932/9955
[INFO] processing image 933/9955
[INFO] processing image 934/9955
[INFO] processing image 935/9955
[INFO] processing image 936/9955
[INFO] processing image 937/9955
[INFO] processing image 938/9955
[INFO] processing image 939/9955
[INFO] processing image 940/9955
[INFO] processing image 941/9955
[INFO] processing image 942/9955
[INFO] processing image 943/9955
[INFO] processing image 944/9955
[INFO] processing image 945/9955
[INFO] processing image 946/9955
[INFO] processing image 947/9955
[INFO] processing image 948/9955
[INFO] processing image 949/9955
[INFO] processing image 950/9955
[INFO] processing image 951/9955
[INFO] processing image 952/9955
[INFO] processing image 953/9955
[INFO] processing image 954/9955
[INFO] processing image 955/9955
[INFO] processing image 956/9955
[INFO] processing image 957/9955
[INFO] processing image 958/9955
[INFO] processing image 959/9955
[INFO] processing image 960/9955
[INFO] processing image 961/9955
[INFO] processing image 962/9955
[INFO] processing image 963/9955
[INFO] processing image 964/9955
[INFO] processing image 965/9955
[INFO] processing image 966/9955
[INFO] processing image 967/9955
[INFO] processing image 968/9955
[INFO] processing image 969/9955
[INFO] processing image 970/9955
[INFO] processing image 971/9955
[INFO] processing image 972/9955
[INFO] processing image 973/9955
[INFO] processing image 974/9955
[INFO] processing image 975/9955
[INFO] processing image 976/9955
[INFO] processing image 977/9955
[INFO] processing image 978/9955
[INFO] processing image 979/9955
[INFO] processing image 980/9955
[INFO] processing image 981/9955
[INFO] processing image 982/9955
[INFO] processing image 983/9955
[INFO] processing image 984/9955
[INFO] processing image 985/9955
[INFO] processing image 986/9955
[INFO] processing image 987/9955
[INFO] processing image 988/9955
[INFO] processing image 989/9955
[INFO] processing image 990/9955
[INFO] processing image 991/9955
[INFO] processing image 992/9955
[INFO] processing image 993/9955
[INFO] processing image 994/9955
[INFO] processing image 995/9955
[INFO] processing image 996/9955
[INFO] processing image 997/9955
[INFO] processing image 998/9955
[INFO] processing image 999/9955
[INFO] processing image 1000/9955
[INFO] processing image 1001/9955
[INFO] processing image 1002/9955
[INFO] processing image 1003/9955
[INFO] processing image 1004/9955
[INFO] processing image 1005/9955
[INFO] processing image 1006/9955
[INFO] processing image 1007/9955
[INFO] processing image 1008/9955
[INFO] processing image 1009/9955
[INFO] processing image 1010/9955
[INFO] processing image 1011/9955
[INFO] processing image 1012/9955
[INFO] processing image 1013/9955
[INFO] processing image 1014/9955
[INFO] processing image 1015/9955
[INFO] processing image 1016/9955
[INFO] processing image 1017/9955
[INFO] processing image 1018/9955
[INFO] processing image 1019/9955
[INFO] processing image 1020/9955
[INFO] processing image 1021/9955
[INFO] processing image 1022/9955
[INFO] processing image 1023/9955
[INFO] processing image 1024/9955
[INFO] processing image 1025/9955
[INFO] processing image 1026/9955
[INFO] processing image 1027/9955
[INFO] processing image 1028/9955
[INFO] processing image 1029/9955
[INFO] processing image 1030/9955
[INFO] processing image 1031/9955
[INFO] processing image 1032/9955
[INFO] processing image 1033/9955
[INFO] processing image 1034/9955
[INFO] processing image 1035/9955
[INFO] processing image 1036/9955
[INFO] processing image 1037/9955
[INFO] processing image 1038/9955
[INFO] processing image 1039/9955
[INFO] processing image 1040/9955
[INFO] processing image 1041/9955
[INFO] processing image 1042/9955
[INFO] processing image 1043/9955
[INFO] processing image 1044/9955
[INFO] processing image 1045/9955
[INFO] processing image 1046/9955
[INFO] processing image 1047/9955
[INFO] processing image 1048/9955
[INFO] processing image 1049/9955
[INFO] processing image 1050/9955
[INFO] processing image 1051/9955
[INFO] processing image 1052/9955
[INFO] processing image 1053/9955
[INFO] processing image 1054/9955
[INFO] processing image 1055/9955
[INFO] processing image 1056/9955
[INFO] processing image 1057/9955
[INFO] processing image 1058/9955
[INFO] processing image 1059/9955
[INFO] processing image 1060/9955
[INFO] processing image 1061/9955
[INFO] processing image 1062/9955
[INFO] processing image 1063/9955
[INFO] processing image 1064/9955
[INFO] processing image 1065/9955
[INFO] processing image 1066/9955
[INFO] processing image 1067/9955
[INFO] processing image 1068/9955
[INFO] processing image 1069/9955
[INFO] processing image 1070/9955
[INFO] processing image 1071/9955
[INFO] processing image 1072/9955
[INFO] processing image 1073/9955
[INFO] processing image 1074/9955
[INFO] processing image 1075/9955
[INFO] processing image 1076/9955
[INFO] processing image 1077/9955
[INFO] processing image 1078/9955
[INFO] processing image 1079/9955
[INFO] processing image 1080/9955
[INFO] processing image 1081/9955
[INFO] processing image 1082/9955
[INFO] processing image 1083/9955
[INFO] processing image 1084/9955
[INFO] processing image 1085/9955
[INFO] processing image 1086/9955
[INFO] processing image 1087/9955
[INFO] processing image 1088/9955
[INFO] processing image 1089/9955
[INFO] processing image 1090/9955
[INFO] processing image 1091/9955
[INFO] processing image 1092/9955
[INFO] processing image 1093/9955
[INFO] processing image 1094/9955
[INFO] processing image 1095/9955
[INFO] processing image 1096/9955
[INFO] processing image 1097/9955
[INFO] processing image 1098/9955
[INFO] processing image 1099/9955
[INFO] processing image 1100/9955
[INFO] processing image 1101/9955
[INFO] processing image 1102/9955
[INFO] processing image 1103/9955
[INFO] processing image 1104/9955
[INFO] processing image 1105/9955
[INFO] processing image 1106/9955
[INFO] processing image 1107/9955
[INFO] processing image 1108/9955
[INFO] processing image 1109/9955
[INFO] processing image 1110/9955
[INFO] processing image 1111/9955
[INFO] processing image 1112/9955
[INFO] processing image 1113/9955
[INFO] processing image 1114/9955
[INFO] processing image 1115/9955
[INFO] processing image 1116/9955
[INFO] processing image 1117/9955
[INFO] processing image 1118/9955
[INFO] processing image 1119/9955
[INFO] processing image 1120/9955
[INFO] processing image 1121/9955
[INFO] processing image 1122/9955
[INFO] processing image 1123/9955
[INFO] processing image 1124/9955
[INFO] processing image 1125/9955
[INFO] processing image 1126/9955
[INFO] processing image 1127/9955
[INFO] processing image 1128/9955
[INFO] processing image 1129/9955
[INFO] processing image 1130/9955
[INFO] processing image 1131/9955
[INFO] processing image 1132/9955
[INFO] processing image 1133/9955
[INFO] processing image 1134/9955
[INFO] processing image 1135/9955
[INFO] processing image 1136/9955
[INFO] processing image 1137/9955
[INFO] processing image 1138/9955
[INFO] processing image 1139/9955
[INFO] processing image 1140/9955
[INFO] processing image 1141/9955
[INFO] processing image 1142/9955
[INFO] processing image 1143/9955
[INFO] processing image 1144/9955
[INFO] processing image 1145/9955
[INFO] processing image 1146/9955
[INFO] processing image 1147/9955
[INFO] processing image 1148/9955
[INFO] processing image 1149/9955
[INFO] processing image 1150/9955
[INFO] processing image 1151/9955
[INFO] processing image 1152/9955
[INFO] processing image 1153/9955
[INFO] processing image 1154/9955
[INFO] processing image 1155/9955
[INFO] processing image 1156/9955
[INFO] processing image 1157/9955
[INFO] processing image 1158/9955
[INFO] processing image 1159/9955
[INFO] processing image 1160/9955
[INFO] processing image 1161/9955
[INFO] processing image 1162/9955
[INFO] processing image 1163/9955
[INFO] processing image 1164/9955
[INFO] processing image 1165/9955
[INFO] processing image 1166/9955
[INFO] processing image 1167/9955
[INFO] processing image 1168/9955
[INFO] processing image 1169/9955
[INFO] processing image 1170/9955
[INFO] processing image 1171/9955
[INFO] processing image 1172/9955
[INFO] processing image 1173/9955
[INFO] processing image 1174/9955
[INFO] processing image 1175/9955
[INFO] processing image 1176/9955
[INFO] processing image 1177/9955
[INFO] processing image 1178/9955
[INFO] processing image 1179/9955
[INFO] processing image 1180/9955
[INFO] processing image 1181/9955
[INFO] processing image 1182/9955
[INFO] processing image 1183/9955
[INFO] processing image 1184/9955
[INFO] processing image 1185/9955
[INFO] processing image 1186/9955
[INFO] processing image 1187/9955
[INFO] processing image 1188/9955
[INFO] processing image 1189/9955
[INFO] processing image 1190/9955
[INFO] processing image 1191/9955
[INFO] processing image 1192/9955
[INFO] processing image 1193/9955
[INFO] processing image 1194/9955
[INFO] processing image 1195/9955
[INFO] processing image 1196/9955
[INFO] processing image 1197/9955
[INFO] processing image 1198/9955
[INFO] processing image 1199/9955
[INFO] processing image 1200/9955
[INFO] processing image 1201/9955
[INFO] processing image 1202/9955
[INFO] processing image 1203/9955
[INFO] processing image 1204/9955
[INFO] processing image 1205/9955
[INFO] processing image 1206/9955
[INFO] processing image 1207/9955
[INFO] processing image 1208/9955
[INFO] processing image 1209/9955
[INFO] processing image 1210/9955
[INFO] processing image 1211/9955
[INFO] processing image 1212/9955
[INFO] processing image 1213/9955
[INFO] processing image 1214/9955
[INFO] processing image 1215/9955
[INFO] processing image 1216/9955
[INFO] processing image 1217/9955
[INFO] processing image 1218/9955
[INFO] processing image 1219/9955
[INFO] processing image 1220/9955
[INFO] processing image 1221/9955
[INFO] processing image 1222/9955
[INFO] processing image 1223/9955
[INFO] processing image 1224/9955
[INFO] processing image 1225/9955
[INFO] processing image 1226/9955
[INFO] processing image 1227/9955
[INFO] processing image 1228/9955
[INFO] processing image 1229/9955
[INFO] processing image 1230/9955
[INFO] processing image 1231/9955
[INFO] processing image 1232/9955
[INFO] processing image 1233/9955
[INFO] processing image 1234/9955
[INFO] processing image 1235/9955
[INFO] processing image 1236/9955
[INFO] processing image 1237/9955
[INFO] processing image 1238/9955
[INFO] processing image 1239/9955
[INFO] processing image 1240/9955
[INFO] processing image 1241/9955
[INFO] processing image 1242/9955
[INFO] processing image 1243/9955
[INFO] processing image 1244/9955
[INFO] processing image 1245/9955
[INFO] processing image 1246/9955
[INFO] processing image 1247/9955
[INFO] processing image 1248/9955
[INFO] processing image 1249/9955
[INFO] processing image 1250/9955
[INFO] processing image 1251/9955
[INFO] processing image 1252/9955
[INFO] processing image 1253/9955
[INFO] processing image 1254/9955
[INFO] processing image 1255/9955
[INFO] processing image 1256/9955
[INFO] processing image 1257/9955
[INFO] processing image 1258/9955
[INFO] processing image 1259/9955
[INFO] processing image 1260/9955
[INFO] processing image 1261/9955
[INFO] processing image 1262/9955
[INFO] processing image 1263/9955
[INFO] processing image 1264/9955
[INFO] processing image 1265/9955
[INFO] processing image 1266/9955
[INFO] processing image 1267/9955
[INFO] processing image 1268/9955
[INFO] processing image 1269/9955
[INFO] processing image 1270/9955
[INFO] processing image 1271/9955
[INFO] processing image 1272/9955
[INFO] processing image 1273/9955
[INFO] processing image 1274/9955
[INFO] processing image 1275/9955
[INFO] processing image 1276/9955
[INFO] processing image 1277/9955
[INFO] processing image 1278/9955
[INFO] processing image 1279/9955
[INFO] processing image 1280/9955
[INFO] processing image 1281/9955
[INFO] processing image 1282/9955
[INFO] processing image 1283/9955
[INFO] processing image 1284/9955
[INFO] processing image 1285/9955
[INFO] processing image 1286/9955
[INFO] processing image 1287/9955
[INFO] processing image 1288/9955
[INFO] processing image 1289/9955
[INFO] processing image 1290/9955
[INFO] processing image 1291/9955
[INFO] processing image 1292/9955
[INFO] processing image 1293/9955
[INFO] processing image 1294/9955
[INFO] processing image 1295/9955
[INFO] processing image 1296/9955
[INFO] processing image 1297/9955
[INFO] processing image 1298/9955
[INFO] processing image 1299/9955
[INFO] processing image 1300/9955
[INFO] processing image 1301/9955
[INFO] processing image 1302/9955
[INFO] processing image 1303/9955
[INFO] processing image 1304/9955
[INFO] processing image 1305/9955
[INFO] processing image 1306/9955
[INFO] processing image 1307/9955
[INFO] processing image 1308/9955
[INFO] processing image 1309/9955
[INFO] processing image 1310/9955
[INFO] processing image 1311/9955
[INFO] processing image 1312/9955
[INFO] processing image 1313/9955
[INFO] processing image 1314/9955
[INFO] processing image 1315/9955
[INFO] processing image 1316/9955
[INFO] processing image 1317/9955
[INFO] processing image 1318/9955
[INFO] processing image 1319/9955
[INFO] processing image 1320/9955
[INFO] processing image 1321/9955
[INFO] processing image 1322/9955
[INFO] processing image 1323/9955
[INFO] processing image 1324/9955
[INFO] processing image 1325/9955
[INFO] processing image 1326/9955
[INFO] processing image 1327/9955
[INFO] processing image 1328/9955
[INFO] processing image 1329/9955
[INFO] processing image 1330/9955
[INFO] processing image 1331/9955
[INFO] processing image 1332/9955
[INFO] processing image 1333/9955
[INFO] processing image 1334/9955
[INFO] processing image 1335/9955
[INFO] processing image 1336/9955
[INFO] processing image 1337/9955
[INFO] processing image 1338/9955
[INFO] processing image 1339/9955
[INFO] processing image 1340/9955
[INFO] processing image 1341/9955
[INFO] processing image 1342/9955
[INFO] processing image 1343/9955
[INFO] processing image 1344/9955
[INFO] processing image 1345/9955
[INFO] processing image 1346/9955
[INFO] processing image 1347/9955
[INFO] processing image 1348/9955
[INFO] processing image 1349/9955
[INFO] processing image 1350/9955
[INFO] processing image 1351/9955
[INFO] processing image 1352/9955
[INFO] processing image 1353/9955
[INFO] processing image 1354/9955
[INFO] processing image 1355/9955
[INFO] processing image 1356/9955
[INFO] processing image 1357/9955
[INFO] processing image 1358/9955
[INFO] processing image 1359/9955
[INFO] processing image 1360/9955
[INFO] processing image 1361/9955
[INFO] processing image 1362/9955
[INFO] processing image 1363/9955
[INFO] processing image 1364/9955
[INFO] processing image 1365/9955
[INFO] processing image 1366/9955
[INFO] processing image 1367/9955
[INFO] processing image 1368/9955
[INFO] processing image 1369/9955
[INFO] processing image 1370/9955
[INFO] processing image 1371/9955
[INFO] processing image 1372/9955
[INFO] processing image 1373/9955
[INFO] processing image 1374/9955
[INFO] processing image 1375/9955
[INFO] processing image 1376/9955
[INFO] processing image 1377/9955
[INFO] processing image 1378/9955
[INFO] processing image 1379/9955
[INFO] processing image 1380/9955
[INFO] processing image 1381/9955
[INFO] processing image 1382/9955
[INFO] processing image 1383/9955
[INFO] processing image 1384/9955
[INFO] processing image 1385/9955
[INFO] processing image 1386/9955
[INFO] processing image 1387/9955
[INFO] processing image 1388/9955
[INFO] processing image 1389/9955
[INFO] processing image 1390/9955
[INFO] processing image 1391/9955
[INFO] processing image 1392/9955
[INFO] processing image 1393/9955
[INFO] processing image 1394/9955
[INFO] processing image 1395/9955
[INFO] processing image 1396/9955
[INFO] processing image 1397/9955
[INFO] processing image 1398/9955
[INFO] processing image 1399/9955
[INFO] processing image 1400/9955
[INFO] processing image 1401/9955
[INFO] processing image 1402/9955
[INFO] processing image 1403/9955
[INFO] processing image 1404/9955
[INFO] processing image 1405/9955
[INFO] processing image 1406/9955
[INFO] processing image 1407/9955
[INFO] processing image 1408/9955
[INFO] processing image 1409/9955
[INFO] processing image 1410/9955
[INFO] processing image 1411/9955
[INFO] processing image 1412/9955
[INFO] processing image 1413/9955
[INFO] processing image 1414/9955
[INFO] processing image 1415/9955
[INFO] processing image 1416/9955
[INFO] processing image 1417/9955
[INFO] processing image 1418/9955
[INFO] processing image 1419/9955
[INFO] processing image 1420/9955
[INFO] processing image 1421/9955
[INFO] processing image 1422/9955
[INFO] processing image 1423/9955
[INFO] processing image 1424/9955
[INFO] processing image 1425/9955
[INFO] processing image 1426/9955
[INFO] processing image 1427/9955
[INFO] processing image 1428/9955
[INFO] processing image 1429/9955
[INFO] processing image 1430/9955
[INFO] processing image 1431/9955
[INFO] processing image 1432/9955
[INFO] processing image 1433/9955
[INFO] processing image 1434/9955
[INFO] processing image 1435/9955
[INFO] processing image 1436/9955
[INFO] processing image 1437/9955
[INFO] processing image 1438/9955
[INFO] processing image 1439/9955
[INFO] processing image 1440/9955
[INFO] processing image 1441/9955
[INFO] processing image 1442/9955
[INFO] processing image 1443/9955
[INFO] processing image 1444/9955
[INFO] processing image 1445/9955
[INFO] processing image 1446/9955
[INFO] processing image 1447/9955
[INFO] processing image 1448/9955
[INFO] processing image 1449/9955
[INFO] processing image 1450/9955
[INFO] processing image 1451/9955
[INFO] processing image 1452/9955
[INFO] processing image 1453/9955
[INFO] processing image 1454/9955
[INFO] processing image 1455/9955
[INFO] processing image 1456/9955
[INFO] processing image 1457/9955
[INFO] processing image 1458/9955
[INFO] processing image 1459/9955
[INFO] processing image 1460/9955
[INFO] processing image 1461/9955
[INFO] processing image 1462/9955
[INFO] processing image 1463/9955
[INFO] processing image 1464/9955
[INFO] processing image 1465/9955
[INFO] processing image 1466/9955
[INFO] processing image 1467/9955
[INFO] processing image 1468/9955
[INFO] processing image 1469/9955
[INFO] processing image 1470/9955
[INFO] processing image 1471/9955
[INFO] processing image 1472/9955
[INFO] processing image 1473/9955
[INFO] processing image 1474/9955
[INFO] processing image 1475/9955
[INFO] processing image 1476/9955
[INFO] processing image 1477/9955
[INFO] processing image 1478/9955
[INFO] processing image 1479/9955
[INFO] processing image 1480/9955
[INFO] processing image 1481/9955
[INFO] processing image 1482/9955
[INFO] processing image 1483/9955
[INFO] processing image 1484/9955
[INFO] processing image 1485/9955
[INFO] processing image 1486/9955
[INFO] processing image 1487/9955
[INFO] processing image 1488/9955
[INFO] processing image 1489/9955
[INFO] processing image 1490/9955
[INFO] processing image 1491/9955
[INFO] processing image 1492/9955
[INFO] processing image 1493/9955
[INFO] processing image 1494/9955
[INFO] processing image 1495/9955
[INFO] processing image 1496/9955
[INFO] processing image 1497/9955
[INFO] processing image 1498/9955
[INFO] processing image 1499/9955
[INFO] processing image 1500/9955
[INFO] processing image 1501/9955
[INFO] processing image 1502/9955
[INFO] processing image 1503/9955
[INFO] processing image 1504/9955
[INFO] processing image 1505/9955
[INFO] processing image 1506/9955
[INFO] processing image 1507/9955
[INFO] processing image 1508/9955
[INFO] processing image 1509/9955
[INFO] processing image 1510/9955
[INFO] processing image 1511/9955
[INFO] processing image 1512/9955
[INFO] processing image 1513/9955
[INFO] processing image 1514/9955
[INFO] processing image 1515/9955
[INFO] processing image 1516/9955
[INFO] processing image 1517/9955
[INFO] processing image 1518/9955
[INFO] processing image 1519/9955
[INFO] processing image 1520/9955
[INFO] processing image 1521/9955
[INFO] processing image 1522/9955
[INFO] processing image 1523/9955
[INFO] processing image 1524/9955
[INFO] processing image 1525/9955
[INFO] processing image 1526/9955
[INFO] processing image 1527/9955
[INFO] processing image 1528/9955
[INFO] processing image 1529/9955
[INFO] processing image 1530/9955
[INFO] processing image 1531/9955
[INFO] processing image 1532/9955
[INFO] processing image 1533/9955
[INFO] processing image 1534/9955
[INFO] processing image 1535/9955
[INFO] processing image 1536/9955
[INFO] processing image 1537/9955
[INFO] processing image 1538/9955
[INFO] processing image 1539/9955
[INFO] processing image 1540/9955
[INFO] processing image 1541/9955
[INFO] processing image 1542/9955
[INFO] processing image 1543/9955
[INFO] processing image 1544/9955
[INFO] processing image 1545/9955
[INFO] processing image 1546/9955
[INFO] processing image 1547/9955
[INFO] processing image 1548/9955
[INFO] processing image 1549/9955
[INFO] processing image 1550/9955
[INFO] processing image 1551/9955
[INFO] processing image 1552/9955
[INFO] processing image 1553/9955
[INFO] processing image 1554/9955
[INFO] processing image 1555/9955
[INFO] processing image 1556/9955
[INFO] processing image 1557/9955
[INFO] processing image 1558/9955
[INFO] processing image 1559/9955
[INFO] processing image 1560/9955
[INFO] processing image 1561/9955
[INFO] processing image 1562/9955
[INFO] processing image 1563/9955
[INFO] processing image 1564/9955
[INFO] processing image 1565/9955
[INFO] processing image 1566/9955
[INFO] processing image 1567/9955
[INFO] processing image 1568/9955
[INFO] processing image 1569/9955
[INFO] processing image 1570/9955
[INFO] processing image 1571/9955
[INFO] processing image 1572/9955
[INFO] processing image 1573/9955
[INFO] processing image 1574/9955
[INFO] processing image 1575/9955
[INFO] processing image 1576/9955
[INFO] processing image 1577/9955
[INFO] processing image 1578/9955
[INFO] processing image 1579/9955
[INFO] processing image 1580/9955
[INFO] processing image 1581/9955
[INFO] processing image 1582/9955
[INFO] processing image 1583/9955
[INFO] processing image 1584/9955
[INFO] processing image 1585/9955
[INFO] processing image 1586/9955
[INFO] processing image 1587/9955
[INFO] processing image 1588/9955
[INFO] processing image 1589/9955
[INFO] processing image 1590/9955
[INFO] processing image 1591/9955
[INFO] processing image 1592/9955
[INFO] processing image 1593/9955
[INFO] processing image 1594/9955
[INFO] processing image 1595/9955
[INFO] processing image 1596/9955
[INFO] processing image 1597/9955
[INFO] processing image 1598/9955
[INFO] processing image 1599/9955
[INFO] processing image 1600/9955
[INFO] processing image 1601/9955
[INFO] processing image 1602/9955
[INFO] processing image 1603/9955
[INFO] processing image 1604/9955
[INFO] processing image 1605/9955
[INFO] processing image 1606/9955
[INFO] processing image 1607/9955
[INFO] processing image 1608/9955
[INFO] processing image 1609/9955
[INFO] processing image 1610/9955
[INFO] processing image 1611/9955
[INFO] processing image 1612/9955
[INFO] processing image 1613/9955
[INFO] processing image 1614/9955
[INFO] processing image 1615/9955
[INFO] processing image 1616/9955
[INFO] processing image 1617/9955
[INFO] processing image 1618/9955
[INFO] processing image 1619/9955
[INFO] processing image 1620/9955
[INFO] processing image 1621/9955
[INFO] processing image 1622/9955
[INFO] processing image 1623/9955
[INFO] processing image 1624/9955
[INFO] processing image 1625/9955
[INFO] processing image 1626/9955
[INFO] processing image 1627/9955
[INFO] processing image 1628/9955
[INFO] processing image 1629/9955
[INFO] processing image 1630/9955
[INFO] processing image 1631/9955
[INFO] processing image 1632/9955
[INFO] processing image 1633/9955
[INFO] processing image 1634/9955
[INFO] processing image 1635/9955
[INFO] processing image 1636/9955
[INFO] processing image 1637/9955
[INFO] processing image 1638/9955
[INFO] processing image 1639/9955
[INFO] processing image 1640/9955
[INFO] processing image 1641/9955
[INFO] processing image 1642/9955
[INFO] processing image 1643/9955
[INFO] processing image 1644/9955
[INFO] processing image 1645/9955
[INFO] processing image 1646/9955
[INFO] processing image 1647/9955
[INFO] processing image 1648/9955
[INFO] processing image 1649/9955
[INFO] processing image 1650/9955
[INFO] processing image 1651/9955
[INFO] processing image 1652/9955
[INFO] processing image 1653/9955
[INFO] processing image 1654/9955
[INFO] processing image 1655/9955
[INFO] processing image 1656/9955
[INFO] processing image 1657/9955
[INFO] processing image 1658/9955
[INFO] processing image 1659/9955
[INFO] processing image 1660/9955
[INFO] processing image 1661/9955
[INFO] processing image 1662/9955
[INFO] processing image 1663/9955
[INFO] processing image 1664/9955
[INFO] processing image 1665/9955
[INFO] processing image 1666/9955
[INFO] processing image 1667/9955
[INFO] processing image 1668/9955
[INFO] processing image 1669/9955
[INFO] processing image 1670/9955
[INFO] processing image 1671/9955
[INFO] processing image 1672/9955
[INFO] processing image 1673/9955
[INFO] processing image 1674/9955
[INFO] processing image 1675/9955
[INFO] processing image 1676/9955
[INFO] processing image 1677/9955
[INFO] processing image 1678/9955
[INFO] processing image 1679/9955
[INFO] processing image 1680/9955
[INFO] processing image 1681/9955
[INFO] processing image 1682/9955
[INFO] processing image 1683/9955
[INFO] processing image 1684/9955
[INFO] processing image 1685/9955
[INFO] processing image 1686/9955
[INFO] processing image 1687/9955
[INFO] processing image 1688/9955
[INFO] processing image 1689/9955
[INFO] processing image 1690/9955
[INFO] processing image 1691/9955
[INFO] processing image 1692/9955
[INFO] processing image 1693/9955
[INFO] processing image 1694/9955
[INFO] processing image 1695/9955
[INFO] processing image 1696/9955
[INFO] processing image 1697/9955
[INFO] processing image 1698/9955
[INFO] processing image 1699/9955
[INFO] processing image 1700/9955
[INFO] processing image 1701/9955
[INFO] processing image 1702/9955
[INFO] processing image 1703/9955
[INFO] processing image 1704/9955
[INFO] processing image 1705/9955
[INFO] processing image 1706/9955
[INFO] processing image 1707/9955
[INFO] processing image 1708/9955
[INFO] processing image 1709/9955
[INFO] processing image 1710/9955
[INFO] processing image 1711/9955
[INFO] processing image 1712/9955
[INFO] processing image 1713/9955
[INFO] processing image 1714/9955
[INFO] processing image 1715/9955
[INFO] processing image 1716/9955
[INFO] processing image 1717/9955
[INFO] processing image 1718/9955
[INFO] processing image 1719/9955
[INFO] processing image 1720/9955
[INFO] processing image 1721/9955
[INFO] processing image 1722/9955
[INFO] processing image 1723/9955
[INFO] processing image 1724/9955
[INFO] processing image 1725/9955
[INFO] processing image 1726/9955
[INFO] processing image 1727/9955
[INFO] processing image 1728/9955
[INFO] processing image 1729/9955
[INFO] processing image 1730/9955
[INFO] processing image 1731/9955
[INFO] processing image 1732/9955
[INFO] processing image 1733/9955
[INFO] processing image 1734/9955
[INFO] processing image 1735/9955
[INFO] processing image 1736/9955
[INFO] processing image 1737/9955
[INFO] processing image 1738/9955
[INFO] processing image 1739/9955
[INFO] processing image 1740/9955
[INFO] processing image 1741/9955
[INFO] processing image 1742/9955
[INFO] processing image 1743/9955
[INFO] processing image 1744/9955
[INFO] processing image 1745/9955
[INFO] processing image 1746/9955
[INFO] processing image 1747/9955
[INFO] processing image 1748/9955
[INFO] processing image 1749/9955
[INFO] processing image 1750/9955
[INFO] processing image 1751/9955
[INFO] processing image 1752/9955
[INFO] processing image 1753/9955
[INFO] processing image 1754/9955
[INFO] processing image 1755/9955
[INFO] processing image 1756/9955
[INFO] processing image 1757/9955
[INFO] processing image 1758/9955
[INFO] processing image 1759/9955
[INFO] processing image 1760/9955
[INFO] processing image 1761/9955
[INFO] processing image 1762/9955
[INFO] processing image 1763/9955
[INFO] processing image 1764/9955
[INFO] processing image 1765/9955
[INFO] processing image 1766/9955
[INFO] processing image 1767/9955
[INFO] processing image 1768/9955
[INFO] processing image 1769/9955
[INFO] processing image 1770/9955
[INFO] processing image 1771/9955
[INFO] processing image 1772/9955
[INFO] processing image 1773/9955
[INFO] processing image 1774/9955
[INFO] processing image 1775/9955
[INFO] processing image 1776/9955
[INFO] processing image 1777/9955
[INFO] processing image 1778/9955
[INFO] processing image 1779/9955
[INFO] processing image 1780/9955
[INFO] processing image 1781/9955
[INFO] processing image 1782/9955
[INFO] processing image 1783/9955
[INFO] processing image 1784/9955
[INFO] processing image 1785/9955
[INFO] processing image 1786/9955
[INFO] processing image 1787/9955
[INFO] processing image 1788/9955
[INFO] processing image 1789/9955
[INFO] processing image 1790/9955
[INFO] processing image 1791/9955
[INFO] processing image 1792/9955
[INFO] processing image 1793/9955
[INFO] processing image 1794/9955
[INFO] processing image 1795/9955
[INFO] processing image 1796/9955
[INFO] processing image 1797/9955
[INFO] processing image 1798/9955
[INFO] processing image 1799/9955
[INFO] processing image 1800/9955
[INFO] processing image 1801/9955
[INFO] processing image 1802/9955
[INFO] processing image 1803/9955
[INFO] processing image 1804/9955
[INFO] processing image 1805/9955
[INFO] processing image 1806/9955
[INFO] processing image 1807/9955
[INFO] processing image 1808/9955
[INFO] processing image 1809/9955
[INFO] processing image 1810/9955
[INFO] processing image 1811/9955
[INFO] processing image 1812/9955
[INFO] processing image 1813/9955
[INFO] processing image 1814/9955
[INFO] processing image 1815/9955
[INFO] processing image 1816/9955
[INFO] processing image 1817/9955
[INFO] processing image 1818/9955
[INFO] processing image 1819/9955
[INFO] processing image 1820/9955
[INFO] processing image 1821/9955
[INFO] processing image 1822/9955
[INFO] processing image 1823/9955
[INFO] processing image 1824/9955
[INFO] processing image 1825/9955
[INFO] processing image 1826/9955
[INFO] processing image 1827/9955
[INFO] processing image 1828/9955
[INFO] processing image 1829/9955
[INFO] processing image 1830/9955
[INFO] processing image 1831/9955
[INFO] processing image 1832/9955
[INFO] processing image 1833/9955
[INFO] processing image 1834/9955
[INFO] processing image 1835/9955
[INFO] processing image 1836/9955
[INFO] processing image 1837/9955
[INFO] processing image 1838/9955
[INFO] processing image 1839/9955
[INFO] processing image 1840/9955
[INFO] processing image 1841/9955
[INFO] processing image 1842/9955
[INFO] processing image 1843/9955
[INFO] processing image 1844/9955
[INFO] processing image 1845/9955
[INFO] processing image 1846/9955
[INFO] processing image 1847/9955
[INFO] processing image 1848/9955
[INFO] processing image 1849/9955
[INFO] processing image 1850/9955
[INFO] processing image 1851/9955
[INFO] processing image 1852/9955
[INFO] processing image 1853/9955
[INFO] processing image 1854/9955
[INFO] processing image 1855/9955
[INFO] processing image 1856/9955
[INFO] processing image 1857/9955
[INFO] processing image 1858/9955
[INFO] processing image 1859/9955
[INFO] processing image 1860/9955
[INFO] processing image 1861/9955
[INFO] processing image 1862/9955
[INFO] processing image 1863/9955
[INFO] processing image 1864/9955
[INFO] processing image 1865/9955
[INFO] processing image 1866/9955
[INFO] processing image 1867/9955
[INFO] processing image 1868/9955
[INFO] processing image 1869/9955
[INFO] processing image 1870/9955
[INFO] processing image 1871/9955
[INFO] processing image 1872/9955
[INFO] processing image 1873/9955
[INFO] processing image 1874/9955
[INFO] processing image 1875/9955
[INFO] processing image 1876/9955
[INFO] processing image 1877/9955
[INFO] processing image 1878/9955
[INFO] processing image 1879/9955
[INFO] processing image 1880/9955
[INFO] processing image 1881/9955
[INFO] processing image 1882/9955
[INFO] processing image 1883/9955
[INFO] processing image 1884/9955
[INFO] processing image 1885/9955
[INFO] processing image 1886/9955
[INFO] processing image 1887/9955
[INFO] processing image 1888/9955
[INFO] processing image 1889/9955
[INFO] processing image 1890/9955
[INFO] processing image 1891/9955
[INFO] processing image 1892/9955
[INFO] processing image 1893/9955
[INFO] processing image 1894/9955
[INFO] processing image 1895/9955
[INFO] processing image 1896/9955
[INFO] processing image 1897/9955
[INFO] processing image 1898/9955
[INFO] processing image 1899/9955
[INFO] processing image 1900/9955
[INFO] processing image 1901/9955
[INFO] processing image 1902/9955
[INFO] processing image 1903/9955
[INFO] processing image 1904/9955
[INFO] processing image 1905/9955
[INFO] processing image 1906/9955
[INFO] processing image 1907/9955
[INFO] processing image 1908/9955
[INFO] processing image 1909/9955
[INFO] processing image 1910/9955
[INFO] processing image 1911/9955
[INFO] processing image 1912/9955
[INFO] processing image 1913/9955
[INFO] processing image 1914/9955
[INFO] processing image 1915/9955
[INFO] processing image 1916/9955
[INFO] processing image 1917/9955
[INFO] processing image 1918/9955
[INFO] processing image 1919/9955
[INFO] processing image 1920/9955
[INFO] processing image 1921/9955
[INFO] processing image 1922/9955
[INFO] processing image 1923/9955
[INFO] processing image 1924/9955
[INFO] processing image 1925/9955
[INFO] processing image 1926/9955
[INFO] processing image 1927/9955
[INFO] processing image 1928/9955
[INFO] processing image 1929/9955
[INFO] processing image 1930/9955
[INFO] processing image 1931/9955
[INFO] processing image 1932/9955
[INFO] processing image 1933/9955
[INFO] processing image 1934/9955
[INFO] processing image 1935/9955
[INFO] processing image 1936/9955
[INFO] processing image 1937/9955
[INFO] processing image 1938/9955
[INFO] processing image 1939/9955
[INFO] processing image 1940/9955
[INFO] processing image 1941/9955
[INFO] processing image 1942/9955
[INFO] processing image 1943/9955
[INFO] processing image 1944/9955
[INFO] processing image 1945/9955
[INFO] processing image 1946/9955
[INFO] processing image 1947/9955
[INFO] processing image 1948/9955
[INFO] processing image 1949/9955
[INFO] processing image 1950/9955
[INFO] processing image 1951/9955
[INFO] processing image 1952/9955
[INFO] processing image 1953/9955
[INFO] processing image 1954/9955
[INFO] processing image 1955/9955
[INFO] processing image 1956/9955
[INFO] processing image 1957/9955
[INFO] processing image 1958/9955
[INFO] processing image 1959/9955
[INFO] processing image 1960/9955
[INFO] processing image 1961/9955
[INFO] processing image 1962/9955
[INFO] processing image 1963/9955
[INFO] processing image 1964/9955
[INFO] processing image 1965/9955
[INFO] processing image 1966/9955
[INFO] processing image 1967/9955
[INFO] processing image 1968/9955
[INFO] processing image 1969/9955
[INFO] processing image 1970/9955
[INFO] processing image 1971/9955
[INFO] processing image 1972/9955
[INFO] processing image 1973/9955
[INFO] processing image 1974/9955
[INFO] processing image 1975/9955
[INFO] processing image 1976/9955
[INFO] processing image 1977/9955
[INFO] processing image 1978/9955
[INFO] processing image 1979/9955
[INFO] processing image 1980/9955
[INFO] processing image 1981/9955
[INFO] processing image 1982/9955
[INFO] processing image 1983/9955
[INFO] processing image 1984/9955
[INFO] processing image 1985/9955
[INFO] processing image 1986/9955
[INFO] processing image 1987/9955
[INFO] processing image 1988/9955
[INFO] processing image 1989/9955
[INFO] processing image 1990/9955
[INFO] processing image 1991/9955
[INFO] processing image 1992/9955
[INFO] processing image 1993/9955
[INFO] processing image 1994/9955
[INFO] processing image 1995/9955
[INFO] processing image 1996/9955
[INFO] processing image 1997/9955
[INFO] processing image 1998/9955
[INFO] processing image 1999/9955
[INFO] processing image 2000/9955
[INFO] processing image 2001/9955
[INFO] processing image 2002/9955
[INFO] processing image 2003/9955
[INFO] processing image 2004/9955
[INFO] processing image 2005/9955
[INFO] processing image 2006/9955
[INFO] processing image 2007/9955
[INFO] processing image 2008/9955
[INFO] processing image 2009/9955
[INFO] processing image 2010/9955
[INFO] processing image 2011/9955
[INFO] processing image 2012/9955
[INFO] processing image 2013/9955
[INFO] processing image 2014/9955
[INFO] processing image 2015/9955
[INFO] processing image 2016/9955
[INFO] processing image 2017/9955
[INFO] processing image 2018/9955
[INFO] processing image 2019/9955
[INFO] processing image 2020/9955
[INFO] processing image 2021/9955
[INFO] processing image 2022/9955
[INFO] processing image 2023/9955
[INFO] processing image 2024/9955
[INFO] processing image 2025/9955
[INFO] processing image 2026/9955
[INFO] processing image 2027/9955
[INFO] processing image 2028/9955
[INFO] processing image 2029/9955
[INFO] processing image 2030/9955
[INFO] processing image 2031/9955
[INFO] processing image 2032/9955
[INFO] processing image 2033/9955
[INFO] processing image 2034/9955
[INFO] processing image 2035/9955
[INFO] processing image 2036/9955
[INFO] processing image 2037/9955
[INFO] processing image 2038/9955
[INFO] processing image 2039/9955
[INFO] processing image 2040/9955
[INFO] processing image 2041/9955
[INFO] processing image 2042/9955
[INFO] processing image 2043/9955
[INFO] processing image 2044/9955
[INFO] processing image 2045/9955
[INFO] processing image 2046/9955
[INFO] processing image 2047/9955
[INFO] processing image 2048/9955
[INFO] processing image 2049/9955
[INFO] processing image 2050/9955
[INFO] processing image 2051/9955
[INFO] processing image 2052/9955
[INFO] processing image 2053/9955
[INFO] processing image 2054/9955
[INFO] processing image 2055/9955
[INFO] processing image 2056/9955
[INFO] processing image 2057/9955
[INFO] processing image 2058/9955
[INFO] processing image 2059/9955
[INFO] processing image 2060/9955
[INFO] processing image 2061/9955
[INFO] processing image 2062/9955
[INFO] processing image 2063/9955
[INFO] processing image 2064/9955
[INFO] processing image 2065/9955
[INFO] processing image 2066/9955
[INFO] processing image 2067/9955
[INFO] processing image 2068/9955
[INFO] processing image 2069/9955
[INFO] processing image 2070/9955
[INFO] processing image 2071/9955
[INFO] processing image 2072/9955
[INFO] processing image 2073/9955
[INFO] processing image 2074/9955
[INFO] processing image 2075/9955
[INFO] processing image 2076/9955
[INFO] processing image 2077/9955
[INFO] processing image 2078/9955
[INFO] processing image 2079/9955
[INFO] processing image 2080/9955
[INFO] processing image 2081/9955
[INFO] processing image 2082/9955
[INFO] processing image 2083/9955
[INFO] processing image 2084/9955
[INFO] processing image 2085/9955
[INFO] processing image 2086/9955
[INFO] processing image 2087/9955
[INFO] processing image 2088/9955
[INFO] processing image 2089/9955
[INFO] processing image 2090/9955
[INFO] processing image 2091/9955
[INFO] processing image 2092/9955
[INFO] processing image 2093/9955
[INFO] processing image 2094/9955
[INFO] processing image 2095/9955
[INFO] processing image 2096/9955
[INFO] processing image 2097/9955
[INFO] processing image 2098/9955
[INFO] processing image 2099/9955
[INFO] processing image 2100/9955
[INFO] processing image 2101/9955
[INFO] processing image 2102/9955
[INFO] processing image 2103/9955
[INFO] processing image 2104/9955
[INFO] processing image 2105/9955
[INFO] processing image 2106/9955
[INFO] processing image 2107/9955
[INFO] processing image 2108/9955
[INFO] processing image 2109/9955
[INFO] processing image 2110/9955
[INFO] processing image 2111/9955
[INFO] processing image 2112/9955
[INFO] processing image 2113/9955
[INFO] processing image 2114/9955
[INFO] processing image 2115/9955
[INFO] processing image 2116/9955
[INFO] processing image 2117/9955
[INFO] processing image 2118/9955
[INFO] processing image 2119/9955
[INFO] processing image 2120/9955
[INFO] processing image 2121/9955
[INFO] processing image 2122/9955
[INFO] processing image 2123/9955
[INFO] processing image 2124/9955
[INFO] processing image 2125/9955
[INFO] processing image 2126/9955
[INFO] processing image 2127/9955
[INFO] processing image 2128/9955
[INFO] processing image 2129/9955
[INFO] processing image 2130/9955
[INFO] processing image 2131/9955
[INFO] processing image 2132/9955
[INFO] processing image 2133/9955
[INFO] processing image 2134/9955
[INFO] processing image 2135/9955
[INFO] processing image 2136/9955
[INFO] processing image 2137/9955
[INFO] processing image 2138/9955
[INFO] processing image 2139/9955
[INFO] processing image 2140/9955
[INFO] processing image 2141/9955
[INFO] processing image 2142/9955
[INFO] processing image 2143/9955
[INFO] processing image 2144/9955
[INFO] processing image 2145/9955
[INFO] processing image 2146/9955
[INFO] processing image 2147/9955
[INFO] processing image 2148/9955
[INFO] processing image 2149/9955
[INFO] processing image 2150/9955
[INFO] processing image 2151/9955
[INFO] processing image 2152/9955
[INFO] processing image 2153/9955
[INFO] processing image 2154/9955
[INFO] processing image 2155/9955
[INFO] processing image 2156/9955
[INFO] processing image 2157/9955
[INFO] processing image 2158/9955
[INFO] processing image 2159/9955
[INFO] processing image 2160/9955
[INFO] processing image 2161/9955
[INFO] processing image 2162/9955
[INFO] processing image 2163/9955
[INFO] processing image 2164/9955
[INFO] processing image 2165/9955
[INFO] processing image 2166/9955
[INFO] processing image 2167/9955
[INFO] processing image 2168/9955
[INFO] processing image 2169/9955
[INFO] processing image 2170/9955
[INFO] processing image 2171/9955
[INFO] processing image 2172/9955
[INFO] processing image 2173/9955
[INFO] processing image 2174/9955
[INFO] processing image 2175/9955
[INFO] processing image 2176/9955
[INFO] processing image 2177/9955
[INFO] processing image 2178/9955
[INFO] processing image 2179/9955
[INFO] processing image 2180/9955
[INFO] processing image 2181/9955
[INFO] processing image 2182/9955
[INFO] processing image 2183/9955
[INFO] processing image 2184/9955
[INFO] processing image 2185/9955
[INFO] processing image 2186/9955
[INFO] processing image 2187/9955
[INFO] processing image 2188/9955
[INFO] processing image 2189/9955
[INFO] processing image 2190/9955
[INFO] processing image 2191/9955
[INFO] processing image 2192/9955
[INFO] processing image 2193/9955
[INFO] processing image 2194/9955
[INFO] processing image 2195/9955
[INFO] processing image 2196/9955
[INFO] processing image 2197/9955
[INFO] processing image 2198/9955
[INFO] processing image 2199/9955
[INFO] processing image 2200/9955
[INFO] processing image 2201/9955
[INFO] processing image 2202/9955
[INFO] processing image 2203/9955
[INFO] processing image 2204/9955
[INFO] processing image 2205/9955
[INFO] processing image 2206/9955
[INFO] processing image 2207/9955
[INFO] processing image 2208/9955
[INFO] processing image 2209/9955
[INFO] processing image 2210/9955
[INFO] processing image 2211/9955
[INFO] processing image 2212/9955
[INFO] processing image 2213/9955
[INFO] processing image 2214/9955
[INFO] processing image 2215/9955
[INFO] processing image 2216/9955
[INFO] processing image 2217/9955
[INFO] processing image 2218/9955
[INFO] processing image 2219/9955
[INFO] processing image 2220/9955
[INFO] processing image 2221/9955
[INFO] processing image 2222/9955
[INFO] processing image 2223/9955
[INFO] processing image 2224/9955
[INFO] processing image 2225/9955
[INFO] processing image 2226/9955
[INFO] processing image 2227/9955
[INFO] processing image 2228/9955
[INFO] processing image 2229/9955
[INFO] processing image 2230/9955
[INFO] processing image 2231/9955
[INFO] processing image 2232/9955
[INFO] processing image 2233/9955
[INFO] processing image 2234/9955
[INFO] processing image 2235/9955
[INFO] processing image 2236/9955
[INFO] processing image 2237/9955
[INFO] processing image 2238/9955
[INFO] processing image 2239/9955
[INFO] processing image 2240/9955
[INFO] processing image 2241/9955
[INFO] processing image 2242/9955
[INFO] processing image 2243/9955
[INFO] processing image 2244/9955
[INFO] processing image 2245/9955
[INFO] processing image 2246/9955
[INFO] processing image 2247/9955
[INFO] processing image 2248/9955
[INFO] processing image 2249/9955
[INFO] processing image 2250/9955
[INFO] processing image 2251/9955
[INFO] processing image 2252/9955
[INFO] processing image 2253/9955
[INFO] processing image 2254/9955
[INFO] processing image 2255/9955
[INFO] processing image 2256/9955
[INFO] processing image 2257/9955
[INFO] processing image 2258/9955
[INFO] processing image 2259/9955
[INFO] processing image 2260/9955
[INFO] processing image 2261/9955
[INFO] processing image 2262/9955
[INFO] processing image 2263/9955
[INFO] processing image 2264/9955
[INFO] processing image 2265/9955
[INFO] processing image 2266/9955
[INFO] processing image 2267/9955
[INFO] processing image 2268/9955
[INFO] processing image 2269/9955
[INFO] processing image 2270/9955
[INFO] processing image 2271/9955
[INFO] processing image 2272/9955
[INFO] processing image 2273/9955
[INFO] processing image 2274/9955
[INFO] processing image 2275/9955
[INFO] processing image 2276/9955
[INFO] processing image 2277/9955
[INFO] processing image 2278/9955
[INFO] processing image 2279/9955
[INFO] processing image 2280/9955
[INFO] processing image 2281/9955
[INFO] processing image 2282/9955
[INFO] processing image 2283/9955
[INFO] processing image 2284/9955
[INFO] processing image 2285/9955
[INFO] processing image 2286/9955
[INFO] processing image 2287/9955
[INFO] processing image 2288/9955
[INFO] processing image 2289/9955
[INFO] processing image 2290/9955
[INFO] processing image 2291/9955
[INFO] processing image 2292/9955
[INFO] processing image 2293/9955
[INFO] processing image 2294/9955
[INFO] processing image 2295/9955
[INFO] processing image 2296/9955
[INFO] processing image 2297/9955
[INFO] processing image 2298/9955
[INFO] processing image 2299/9955
[INFO] processing image 2300/9955
[INFO] processing image 2301/9955
[INFO] processing image 2302/9955
[INFO] processing image 2303/9955
[INFO] processing image 2304/9955
[INFO] processing image 2305/9955
[INFO] processing image 2306/9955
[INFO] processing image 2307/9955
[INFO] processing image 2308/9955
[INFO] processing image 2309/9955
[INFO] processing image 2310/9955
[INFO] processing image 2311/9955
[INFO] processing image 2312/9955
[INFO] processing image 2313/9955
[INFO] processing image 2314/9955
[INFO] processing image 2315/9955
[INFO] processing image 2316/9955
[INFO] processing image 2317/9955
[INFO] processing image 2318/9955
[INFO] processing image 2319/9955
[INFO] processing image 2320/9955
[INFO] processing image 2321/9955
[INFO] processing image 2322/9955
[INFO] processing image 2323/9955
[INFO] processing image 2324/9955
[INFO] processing image 2325/9955
[INFO] processing image 2326/9955
[INFO] processing image 2327/9955
[INFO] processing image 2328/9955
[INFO] processing image 2329/9955
[INFO] processing image 2330/9955
[INFO] processing image 2331/9955
[INFO] processing image 2332/9955
[INFO] processing image 2333/9955
[INFO] processing image 2334/9955
[INFO] processing image 2335/9955
[INFO] processing image 2336/9955
[INFO] processing image 2337/9955
[INFO] processing image 2338/9955
[INFO] processing image 2339/9955
[INFO] processing image 2340/9955
[INFO] processing image 2341/9955
[INFO] processing image 2342/9955
[INFO] processing image 2343/9955
[INFO] processing image 2344/9955
[INFO] processing image 2345/9955
[INFO] processing image 2346/9955
[INFO] processing image 2347/9955
[INFO] processing image 2348/9955
[INFO] processing image 2349/9955
[INFO] processing image 2350/9955
[INFO] processing image 2351/9955
[INFO] processing image 2352/9955
[INFO] processing image 2353/9955
[INFO] processing image 2354/9955
[INFO] processing image 2355/9955
[INFO] processing image 2356/9955
[INFO] processing image 2357/9955
[INFO] processing image 2358/9955
[INFO] processing image 2359/9955
[INFO] processing image 2360/9955
[INFO] processing image 2361/9955
[INFO] processing image 2362/9955
[INFO] processing image 2363/9955
[INFO] processing image 2364/9955
[INFO] processing image 2365/9955
[INFO] processing image 2366/9955
[INFO] processing image 2367/9955
[INFO] processing image 2368/9955
[INFO] processing image 2369/9955
[INFO] processing image 2370/9955
[INFO] processing image 2371/9955
[INFO] processing image 2372/9955
[INFO] processing image 2373/9955
[INFO] processing image 2374/9955
[INFO] processing image 2375/9955
[INFO] processing image 2376/9955
[INFO] processing image 2377/9955
[INFO] processing image 2378/9955
[INFO] processing image 2379/9955
[INFO] processing image 2380/9955
[INFO] processing image 2381/9955
[INFO] processing image 2382/9955
[INFO] processing image 2383/9955
[INFO] processing image 2384/9955
[INFO] processing image 2385/9955
[INFO] processing image 2386/9955
[INFO] processing image 2387/9955
[INFO] processing image 2388/9955
[INFO] processing image 2389/9955
[INFO] processing image 2390/9955
[INFO] processing image 2391/9955
[INFO] processing image 2392/9955
[INFO] processing image 2393/9955
[INFO] processing image 2394/9955
[INFO] processing image 2395/9955
[INFO] processing image 2396/9955
[INFO] processing image 2397/9955
[INFO] processing image 2398/9955
[INFO] processing image 2399/9955
[INFO] processing image 2400/9955
[INFO] processing image 2401/9955
[INFO] processing image 2402/9955
[INFO] processing image 2403/9955
[INFO] processing image 2404/9955
[INFO] processing image 2405/9955
[INFO] processing image 2406/9955
[INFO] processing image 2407/9955
[INFO] processing image 2408/9955
[INFO] processing image 2409/9955
[INFO] processing image 2410/9955
[INFO] processing image 2411/9955
[INFO] processing image 2412/9955
[INFO] processing image 2413/9955
[INFO] processing image 2414/9955
[INFO] processing image 2415/9955
[INFO] processing image 2416/9955
[INFO] processing image 2417/9955
[INFO] processing image 2418/9955
[INFO] processing image 2419/9955
[INFO] processing image 2420/9955
[INFO] processing image 2421/9955
[INFO] processing image 2422/9955
[INFO] processing image 2423/9955
[INFO] processing image 2424/9955
[INFO] processing image 2425/9955
[INFO] processing image 2426/9955
[INFO] processing image 2427/9955
[INFO] processing image 2428/9955
[INFO] processing image 2429/9955
[INFO] processing image 2430/9955
[INFO] processing image 2431/9955
[INFO] processing image 2432/9955
[INFO] processing image 2433/9955
[INFO] processing image 2434/9955
[INFO] processing image 2435/9955
[INFO] processing image 2436/9955
[INFO] processing image 2437/9955
[INFO] processing image 2438/9955
[INFO] processing image 2439/9955
[INFO] processing image 2440/9955
[INFO] processing image 2441/9955
[INFO] processing image 2442/9955
[INFO] processing image 2443/9955
[INFO] processing image 2444/9955
[INFO] processing image 2445/9955
[INFO] processing image 2446/9955
[INFO] processing image 2447/9955
[INFO] processing image 2448/9955
[INFO] processing image 2449/9955
[INFO] processing image 2450/9955
[INFO] processing image 2451/9955
[INFO] processing image 2452/9955
[INFO] processing image 2453/9955
[INFO] processing image 2454/9955
[INFO] processing image 2455/9955
[INFO] processing image 2456/9955
[INFO] processing image 2457/9955
[INFO] processing image 2458/9955
[INFO] processing image 2459/9955
[INFO] processing image 2460/9955
[INFO] processing image 2461/9955
[INFO] processing image 2462/9955
[INFO] processing image 2463/9955
[INFO] processing image 2464/9955
[INFO] processing image 2465/9955
[INFO] processing image 2466/9955
[INFO] processing image 2467/9955
[INFO] processing image 2468/9955
[INFO] processing image 2469/9955
[INFO] processing image 2470/9955
[INFO] processing image 2471/9955
[INFO] processing image 2472/9955
[INFO] processing image 2473/9955
[INFO] processing image 2474/9955
[INFO] processing image 2475/9955
[INFO] processing image 2476/9955
[INFO] processing image 2477/9955
[INFO] processing image 2478/9955
[INFO] processing image 2479/9955
[INFO] processing image 2480/9955
[INFO] processing image 2481/9955
[INFO] processing image 2482/9955
[INFO] processing image 2483/9955
[INFO] processing image 2484/9955
[INFO] processing image 2485/9955
[INFO] processing image 2486/9955
[INFO] processing image 2487/9955
[INFO] processing image 2488/9955
[INFO] processing image 2489/9955
[INFO] processing image 2490/9955
[INFO] processing image 2491/9955
[INFO] processing image 2492/9955
[INFO] processing image 2493/9955
[INFO] processing image 2494/9955
[INFO] processing image 2495/9955
[INFO] processing image 2496/9955
[INFO] processing image 2497/9955
[INFO] processing image 2498/9955
[INFO] processing image 2499/9955
[INFO] processing image 2500/9955
[INFO] processing image 2501/9955
[INFO] processing image 2502/9955
[INFO] processing image 2503/9955
[INFO] processing image 2504/9955
[INFO] processing image 2505/9955
[INFO] processing image 2506/9955
[INFO] processing image 2507/9955
[INFO] processing image 2508/9955
[INFO] processing image 2509/9955
[INFO] processing image 2510/9955
[INFO] processing image 2511/9955
[INFO] processing image 2512/9955
[INFO] processing image 2513/9955
[INFO] processing image 2514/9955
[INFO] processing image 2515/9955
[INFO] processing image 2516/9955
[INFO] processing image 2517/9955
[INFO] processing image 2518/9955
[INFO] processing image 2519/9955
[INFO] processing image 2520/9955
[INFO] processing image 2521/9955
[INFO] processing image 2522/9955
[INFO] processing image 2523/9955
[INFO] processing image 2524/9955
[INFO] processing image 2525/9955
[INFO] processing image 2526/9955
[INFO] processing image 2527/9955
[INFO] processing image 2528/9955
[INFO] processing image 2529/9955
[INFO] processing image 2530/9955
[INFO] processing image 2531/9955
[INFO] processing image 2532/9955
[INFO] processing image 2533/9955
[INFO] processing image 2534/9955
[INFO] processing image 2535/9955
[INFO] processing image 2536/9955
[INFO] processing image 2537/9955
[INFO] processing image 2538/9955
[INFO] processing image 2539/9955
[INFO] processing image 2540/9955
[INFO] processing image 2541/9955
[INFO] processing image 2542/9955
[INFO] processing image 2543/9955
[INFO] processing image 2544/9955
[INFO] processing image 2545/9955
[INFO] processing image 2546/9955
[INFO] processing image 2547/9955
[INFO] processing image 2548/9955
[INFO] processing image 2549/9955
[INFO] processing image 2550/9955
[INFO] processing image 2551/9955
[INFO] processing image 2552/9955
[INFO] processing image 2553/9955
[INFO] processing image 2554/9955
[INFO] processing image 2555/9955
[INFO] processing image 2556/9955
[INFO] processing image 2557/9955
[INFO] processing image 2558/9955
[INFO] processing image 2559/9955
[INFO] processing image 2560/9955
[INFO] processing image 2561/9955
[INFO] processing image 2562/9955
[INFO] processing image 2563/9955
[INFO] processing image 2564/9955
[INFO] processing image 2565/9955
[INFO] processing image 2566/9955
[INFO] processing image 2567/9955
[INFO] processing image 2568/9955
[INFO] processing image 2569/9955
[INFO] processing image 2570/9955
[INFO] processing image 2571/9955
[INFO] processing image 2572/9955
[INFO] processing image 2573/9955
[INFO] processing image 2574/9955
[INFO] processing image 2575/9955
[INFO] processing image 2576/9955
[INFO] processing image 2577/9955
[INFO] processing image 2578/9955
[INFO] processing image 2579/9955
[INFO] processing image 2580/9955
[INFO] processing image 2581/9955
[INFO] processing image 2582/9955
[INFO] processing image 2583/9955
[INFO] processing image 2584/9955
[INFO] processing image 2585/9955
[INFO] processing image 2586/9955
[INFO] processing image 2587/9955
[INFO] processing image 2588/9955
[INFO] processing image 2589/9955
[INFO] processing image 2590/9955
[INFO] processing image 2591/9955
[INFO] processing image 2592/9955
[INFO] processing image 2593/9955
[INFO] processing image 2594/9955
[INFO] processing image 2595/9955
[INFO] processing image 2596/9955
[INFO] processing image 2597/9955
[INFO] processing image 2598/9955
[INFO] processing image 2599/9955
[INFO] processing image 2600/9955
[INFO] processing image 2601/9955
[INFO] processing image 2602/9955
[INFO] processing image 2603/9955
[INFO] processing image 2604/9955
[INFO] processing image 2605/9955
[INFO] processing image 2606/9955
[INFO] processing image 2607/9955
[INFO] processing image 2608/9955
[INFO] processing image 2609/9955
[INFO] processing image 2610/9955
[INFO] processing image 2611/9955
[INFO] processing image 2612/9955
[INFO] processing image 2613/9955
[INFO] processing image 2614/9955
[INFO] processing image 2615/9955
[INFO] processing image 2616/9955
[INFO] processing image 2617/9955
[INFO] processing image 2618/9955
[INFO] processing image 2619/9955
[INFO] processing image 2620/9955
[INFO] processing image 2621/9955
[INFO] processing image 2622/9955
[INFO] processing image 2623/9955
[INFO] processing image 2624/9955
[INFO] processing image 2625/9955
[INFO] processing image 2626/9955
[INFO] processing image 2627/9955
[INFO] processing image 2628/9955
[INFO] processing image 2629/9955
[INFO] processing image 2630/9955
[INFO] processing image 2631/9955
[INFO] processing image 2632/9955
[INFO] processing image 2633/9955
[INFO] processing image 2634/9955
[INFO] processing image 2635/9955
[INFO] processing image 2636/9955
[INFO] processing image 2637/9955
[INFO] processing image 2638/9955
[INFO] processing image 2639/9955
[INFO] processing image 2640/9955
[INFO] processing image 2641/9955
[INFO] processing image 2642/9955
[INFO] processing image 2643/9955
[INFO] processing image 2644/9955
[INFO] processing image 2645/9955
[INFO] processing image 2646/9955
[INFO] processing image 2647/9955
[INFO] processing image 2648/9955
[INFO] processing image 2649/9955
[INFO] processing image 2650/9955
[INFO] processing image 2651/9955
[INFO] processing image 2652/9955
[INFO] processing image 2653/9955
[INFO] processing image 2654/9955
[INFO] processing image 2655/9955
[INFO] processing image 2656/9955
[INFO] processing image 2657/9955
[INFO] processing image 2658/9955
[INFO] processing image 2659/9955
[INFO] processing image 2660/9955
[INFO] processing image 2661/9955
[INFO] processing image 2662/9955
[INFO] processing image 2663/9955
[INFO] processing image 2664/9955
[INFO] processing image 2665/9955
[INFO] processing image 2666/9955
[INFO] processing image 2667/9955
[INFO] processing image 2668/9955
[INFO] processing image 2669/9955
[INFO] processing image 2670/9955
[INFO] processing image 2671/9955
[INFO] processing image 2672/9955
[INFO] processing image 2673/9955
[INFO] processing image 2674/9955
[INFO] processing image 2675/9955
[INFO] processing image 2676/9955
[INFO] processing image 2677/9955
[INFO] processing image 2678/9955
[INFO] processing image 2679/9955
[INFO] processing image 2680/9955
[INFO] processing image 2681/9955
[INFO] processing image 2682/9955
[INFO] processing image 2683/9955
[INFO] processing image 2684/9955
[INFO] processing image 2685/9955
[INFO] processing image 2686/9955
[INFO] processing image 2687/9955
[INFO] processing image 2688/9955
[INFO] processing image 2689/9955
[INFO] processing image 2690/9955
[INFO] processing image 2691/9955
[INFO] processing image 2692/9955
[INFO] processing image 2693/9955
[INFO] processing image 2694/9955
[INFO] processing image 2695/9955
[INFO] processing image 2696/9955
[INFO] processing image 2697/9955
[INFO] processing image 2698/9955
[INFO] processing image 2699/9955
[INFO] processing image 2700/9955
[INFO] processing image 2701/9955
[INFO] processing image 2702/9955
[INFO] processing image 2703/9955
[INFO] processing image 2704/9955
[INFO] processing image 2705/9955
[INFO] processing image 2706/9955
[INFO] processing image 2707/9955
[INFO] processing image 2708/9955
[INFO] processing image 2709/9955
[INFO] processing image 2710/9955
[INFO] processing image 2711/9955
[INFO] processing image 2712/9955
[INFO] processing image 2713/9955
[INFO] processing image 2714/9955
[INFO] processing image 2715/9955
[INFO] processing image 2716/9955
[INFO] processing image 2717/9955
[INFO] processing image 2718/9955
[INFO] processing image 2719/9955
[INFO] processing image 2720/9955
[INFO] processing image 2721/9955
[INFO] processing image 2722/9955
[INFO] processing image 2723/9955
[INFO] processing image 2724/9955
[INFO] processing image 2725/9955
[INFO] processing image 2726/9955
[INFO] processing image 2727/9955
[INFO] processing image 2728/9955
[INFO] processing image 2729/9955
[INFO] processing image 2730/9955
[INFO] processing image 2731/9955
[INFO] processing image 2732/9955
[INFO] processing image 2733/9955
[INFO] processing image 2734/9955
[INFO] processing image 2735/9955
[INFO] processing image 2736/9955
[INFO] processing image 2737/9955
[INFO] processing image 2738/9955
[INFO] processing image 2739/9955
[INFO] processing image 2740/9955
[INFO] processing image 2741/9955
[INFO] processing image 2742/9955
[INFO] processing image 2743/9955
[INFO] processing image 2744/9955
[INFO] processing image 2745/9955
[INFO] processing image 2746/9955
[INFO] processing image 2747/9955
[INFO] processing image 2748/9955
[INFO] processing image 2749/9955
[INFO] processing image 2750/9955
[INFO] processing image 2751/9955
[INFO] processing image 2752/9955
[INFO] processing image 2753/9955
[INFO] processing image 2754/9955
[INFO] processing image 2755/9955
[INFO] processing image 2756/9955
[INFO] processing image 2757/9955
[INFO] processing image 2758/9955
[INFO] processing image 2759/9955
[INFO] processing image 2760/9955
[INFO] processing image 2761/9955
[INFO] processing image 2762/9955
[INFO] processing image 2763/9955
[INFO] processing image 2764/9955
[INFO] processing image 2765/9955
[INFO] processing image 2766/9955
[INFO] processing image 2767/9955
[INFO] processing image 2768/9955
[INFO] processing image 2769/9955
[INFO] processing image 2770/9955
[INFO] processing image 2771/9955
[INFO] processing image 2772/9955
[INFO] processing image 2773/9955
[INFO] processing image 2774/9955
[INFO] processing image 2775/9955
[INFO] processing image 2776/9955
[INFO] processing image 2777/9955
[INFO] processing image 2778/9955
[INFO] processing image 2779/9955
[INFO] processing image 2780/9955
[INFO] processing image 2781/9955
[INFO] processing image 2782/9955
[INFO] processing image 2783/9955
[INFO] processing image 2784/9955
[INFO] processing image 2785/9955
[INFO] processing image 2786/9955
[INFO] processing image 2787/9955
[INFO] processing image 2788/9955
[INFO] processing image 2789/9955
[INFO] processing image 2790/9955
[INFO] processing image 2791/9955
[INFO] processing image 2792/9955
[INFO] processing image 2793/9955
[INFO] processing image 2794/9955
[INFO] processing image 2795/9955
[INFO] processing image 2796/9955
[INFO] processing image 2797/9955
[INFO] processing image 2798/9955
[INFO] processing image 2799/9955
[INFO] processing image 2800/9955
[INFO] processing image 2801/9955
[INFO] processing image 2802/9955
[INFO] processing image 2803/9955
[INFO] processing image 2804/9955
[INFO] processing image 2805/9955
[INFO] processing image 2806/9955
[INFO] processing image 2807/9955
[INFO] processing image 2808/9955
[INFO] processing image 2809/9955
[INFO] processing image 2810/9955
[INFO] processing image 2811/9955
[INFO] processing image 2812/9955
[INFO] processing image 2813/9955
[INFO] processing image 2814/9955
[INFO] processing image 2815/9955
[INFO] processing image 2816/9955
[INFO] processing image 2817/9955
[INFO] processing image 2818/9955
[INFO] processing image 2819/9955
[INFO] processing image 2820/9955
[INFO] processing image 2821/9955
[INFO] processing image 2822/9955
[INFO] processing image 2823/9955
[INFO] processing image 2824/9955
[INFO] processing image 2825/9955
[INFO] processing image 2826/9955
[INFO] processing image 2827/9955
[INFO] processing image 2828/9955
[INFO] processing image 2829/9955
[INFO] processing image 2830/9955
[INFO] processing image 2831/9955
[INFO] processing image 2832/9955
[INFO] processing image 2833/9955
[INFO] processing image 2834/9955
[INFO] processing image 2835/9955
[INFO] processing image 2836/9955
[INFO] processing image 2837/9955
[INFO] processing image 2838/9955
[INFO] processing image 2839/9955
[INFO] processing image 2840/9955
[INFO] processing image 2841/9955
[INFO] processing image 2842/9955
[INFO] processing image 2843/9955
[INFO] processing image 2844/9955
[INFO] processing image 2845/9955
[INFO] processing image 2846/9955
[INFO] processing image 2847/9955
[INFO] processing image 2848/9955
[INFO] processing image 2849/9955
[INFO] processing image 2850/9955
[INFO] processing image 2851/9955
[INFO] processing image 2852/9955
[INFO] processing image 2853/9955
[INFO] processing image 2854/9955
[INFO] processing image 2855/9955
[INFO] processing image 2856/9955
[INFO] processing image 2857/9955
[INFO] processing image 2858/9955
[INFO] processing image 2859/9955
[INFO] processing image 2860/9955
[INFO] processing image 2861/9955
[INFO] processing image 2862/9955
[INFO] processing image 2863/9955
[INFO] processing image 2864/9955
[INFO] processing image 2865/9955
[INFO] processing image 2866/9955
[INFO] processing image 2867/9955
[INFO] processing image 2868/9955
[INFO] processing image 2869/9955
[INFO] processing image 2870/9955
[INFO] processing image 2871/9955
[INFO] processing image 2872/9955
[INFO] processing image 2873/9955
[INFO] processing image 2874/9955
[INFO] processing image 2875/9955
[INFO] processing image 2876/9955
[INFO] processing image 2877/9955
[INFO] processing image 2878/9955
[INFO] processing image 2879/9955
[INFO] processing image 2880/9955
[INFO] processing image 2881/9955
[INFO] processing image 2882/9955
[INFO] processing image 2883/9955
[INFO] processing image 2884/9955
[INFO] processing image 2885/9955
[INFO] processing image 2886/9955
[INFO] processing image 2887/9955
[INFO] processing image 2888/9955
[INFO] processing image 2889/9955
[INFO] processing image 2890/9955
[INFO] processing image 2891/9955
[INFO] processing image 2892/9955
[INFO] processing image 2893/9955
[INFO] processing image 2894/9955
[INFO] processing image 2895/9955
[INFO] processing image 2896/9955
[INFO] processing image 2897/9955
[INFO] processing image 2898/9955
[INFO] processing image 2899/9955
[INFO] processing image 2900/9955
[INFO] processing image 2901/9955
[INFO] processing image 2902/9955
[INFO] processing image 2903/9955
[INFO] processing image 2904/9955
[INFO] processing image 2905/9955
[INFO] processing image 2906/9955
[INFO] processing image 2907/9955
[INFO] processing image 2908/9955
[INFO] processing image 2909/9955
[INFO] processing image 2910/9955
[INFO] processing image 2911/9955
[INFO] processing image 2912/9955
[INFO] processing image 2913/9955
[INFO] processing image 2914/9955
[INFO] processing image 2915/9955
[INFO] processing image 2916/9955
[INFO] processing image 2917/9955
[INFO] processing image 2918/9955
[INFO] processing image 2919/9955
[INFO] processing image 2920/9955
[INFO] processing image 2921/9955
[INFO] processing image 2922/9955
[INFO] processing image 2923/9955
[INFO] processing image 2924/9955
[INFO] processing image 2925/9955
[INFO] processing image 2926/9955
[INFO] processing image 2927/9955
[INFO] processing image 2928/9955
[INFO] processing image 2929/9955
[INFO] processing image 2930/9955
[INFO] processing image 2931/9955
[INFO] processing image 2932/9955
[INFO] processing image 2933/9955
[INFO] processing image 2934/9955
[INFO] processing image 2935/9955
[INFO] processing image 2936/9955
[INFO] processing image 2937/9955
[INFO] processing image 2938/9955
[INFO] processing image 2939/9955
[INFO] processing image 2940/9955
[INFO] processing image 2941/9955
[INFO] processing image 2942/9955
[INFO] processing image 2943/9955
[INFO] processing image 2944/9955
[INFO] processing image 2945/9955
[INFO] processing image 2946/9955
[INFO] processing image 2947/9955
[INFO] processing image 2948/9955
[INFO] processing image 2949/9955
[INFO] processing image 2950/9955
[INFO] processing image 2951/9955
[INFO] processing image 2952/9955
[INFO] processing image 2953/9955
[INFO] processing image 2954/9955
[INFO] processing image 2955/9955
[INFO] processing image 2956/9955
[INFO] processing image 2957/9955
[INFO] processing image 2958/9955
[INFO] processing image 2959/9955
[INFO] processing image 2960/9955
[INFO] processing image 2961/9955
[INFO] processing image 2962/9955
[INFO] processing image 2963/9955
[INFO] processing image 2964/9955
[INFO] processing image 2965/9955
[INFO] processing image 2966/9955
[INFO] processing image 2967/9955
[INFO] processing image 2968/9955
[INFO] processing image 2969/9955
[INFO] processing image 2970/9955
[INFO] processing image 2971/9955
[INFO] processing image 2972/9955
[INFO] processing image 2973/9955
[INFO] processing image 2974/9955
[INFO] processing image 2975/9955
[INFO] processing image 2976/9955
[INFO] processing image 2977/9955
[INFO] processing image 2978/9955
[INFO] processing image 2979/9955
[INFO] processing image 2980/9955
[INFO] processing image 2981/9955
[INFO] processing image 2982/9955
[INFO] processing image 2983/9955
[INFO] processing image 2984/9955
[INFO] processing image 2985/9955
[INFO] processing image 2986/9955
[INFO] processing image 2987/9955
[INFO] processing image 2988/9955
[INFO] processing image 2989/9955
[INFO] processing image 2990/9955
[INFO] processing image 2991/9955
[INFO] processing image 2992/9955
[INFO] processing image 2993/9955
[INFO] processing image 2994/9955
[INFO] processing image 2995/9955
[INFO] processing image 2996/9955
[INFO] processing image 2997/9955
[INFO] processing image 2998/9955
[INFO] processing image 2999/9955
[INFO] processing image 3000/9955
[INFO] processing image 3001/9955
[INFO] processing image 3002/9955
[INFO] processing image 3003/9955
[INFO] processing image 3004/9955
[INFO] processing image 3005/9955
[INFO] processing image 3006/9955
[INFO] processing image 3007/9955
[INFO] processing image 3008/9955
[INFO] processing image 3009/9955
[INFO] processing image 3010/9955
[INFO] processing image 3011/9955
[INFO] processing image 3012/9955
[INFO] processing image 3013/9955
[INFO] processing image 3014/9955
[INFO] processing image 3015/9955
[INFO] processing image 3016/9955
[INFO] processing image 3017/9955
[INFO] processing image 3018/9955
[INFO] processing image 3019/9955
[INFO] processing image 3020/9955
[INFO] processing image 3021/9955
[INFO] processing image 3022/9955
[INFO] processing image 3023/9955
[INFO] processing image 3024/9955
[INFO] processing image 3025/9955
[INFO] processing image 3026/9955
[INFO] processing image 3027/9955
[INFO] processing image 3028/9955
[INFO] processing image 3029/9955
[INFO] processing image 3030/9955
[INFO] processing image 3031/9955
[INFO] processing image 3032/9955
[INFO] processing image 3033/9955
[INFO] processing image 3034/9955
[INFO] processing image 3035/9955
[INFO] processing image 3036/9955
[INFO] processing image 3037/9955
[INFO] processing image 3038/9955
[INFO] processing image 3039/9955
[INFO] processing image 3040/9955
[INFO] processing image 3041/9955
[INFO] processing image 3042/9955
[INFO] processing image 3043/9955
[INFO] processing image 3044/9955
[INFO] processing image 3045/9955
[INFO] processing image 3046/9955
[INFO] processing image 3047/9955
[INFO] processing image 3048/9955
[INFO] processing image 3049/9955
[INFO] processing image 3050/9955
[INFO] processing image 3051/9955
[INFO] processing image 3052/9955
[INFO] processing image 3053/9955
[INFO] processing image 3054/9955
[INFO] processing image 3055/9955
[INFO] processing image 3056/9955
[INFO] processing image 3057/9955
[INFO] processing image 3058/9955
[INFO] processing image 3059/9955
[INFO] processing image 3060/9955
[INFO] processing image 3061/9955
[INFO] processing image 3062/9955
[INFO] processing image 3063/9955
[INFO] processing image 3064/9955
[INFO] processing image 3065/9955
[INFO] processing image 3066/9955
[INFO] processing image 3067/9955
[INFO] processing image 3068/9955
[INFO] processing image 3069/9955
[INFO] processing image 3070/9955
[INFO] processing image 3071/9955
[INFO] processing image 3072/9955
[INFO] processing image 3073/9955
[INFO] processing image 3074/9955
[INFO] processing image 3075/9955
[INFO] processing image 3076/9955
[INFO] processing image 3077/9955
[INFO] processing image 3078/9955
[INFO] processing image 3079/9955
[INFO] processing image 3080/9955
[INFO] processing image 3081/9955
[INFO] processing image 3082/9955
[INFO] processing image 3083/9955
[INFO] processing image 3084/9955
[INFO] processing image 3085/9955
[INFO] processing image 3086/9955
[INFO] processing image 3087/9955
[INFO] processing image 3088/9955
[INFO] processing image 3089/9955
[INFO] processing image 3090/9955
[INFO] processing image 3091/9955
[INFO] processing image 3092/9955
[INFO] processing image 3093/9955
[INFO] processing image 3094/9955
[INFO] processing image 3095/9955
[INFO] processing image 3096/9955
[INFO] processing image 3097/9955
[INFO] processing image 3098/9955
[INFO] processing image 3099/9955
[INFO] processing image 3100/9955
[INFO] processing image 3101/9955
[INFO] processing image 3102/9955
[INFO] processing image 3103/9955
[INFO] processing image 3104/9955
[INFO] processing image 3105/9955
[INFO] processing image 3106/9955
[INFO] processing image 3107/9955
[INFO] processing image 3108/9955
[INFO] processing image 3109/9955
[INFO] processing image 3110/9955
[INFO] processing image 3111/9955
[INFO] processing image 3112/9955
[INFO] processing image 3113/9955
[INFO] processing image 3114/9955
[INFO] processing image 3115/9955
[INFO] processing image 3116/9955
[INFO] processing image 3117/9955
[INFO] processing image 3118/9955
[INFO] processing image 3119/9955
[INFO] processing image 3120/9955
[INFO] processing image 3121/9955
[INFO] processing image 3122/9955
[INFO] processing image 3123/9955
[INFO] processing image 3124/9955
[INFO] processing image 3125/9955
[INFO] processing image 3126/9955
[INFO] processing image 3127/9955
[INFO] processing image 3128/9955
[INFO] processing image 3129/9955
[INFO] processing image 3130/9955
[INFO] processing image 3131/9955
[INFO] processing image 3132/9955
[INFO] processing image 3133/9955
[INFO] processing image 3134/9955
[INFO] processing image 3135/9955
[INFO] processing image 3136/9955
[INFO] processing image 3137/9955
[INFO] processing image 3138/9955
[INFO] processing image 3139/9955
[INFO] processing image 3140/9955
[INFO] processing image 3141/9955
[INFO] processing image 3142/9955
[INFO] processing image 3143/9955
[INFO] processing image 3144/9955
[INFO] processing image 3145/9955
[INFO] processing image 3146/9955
[INFO] processing image 3147/9955
[INFO] processing image 3148/9955
[INFO] processing image 3149/9955
[INFO] processing image 3150/9955
[INFO] processing image 3151/9955
[INFO] processing image 3152/9955
[INFO] processing image 3153/9955
[INFO] processing image 3154/9955
[INFO] processing image 3155/9955
[INFO] processing image 3156/9955
[INFO] processing image 3157/9955
[INFO] processing image 3158/9955
[INFO] processing image 3159/9955
[INFO] processing image 3160/9955
[INFO] processing image 3161/9955
[INFO] processing image 3162/9955
[INFO] processing image 3163/9955
[INFO] processing image 3164/9955
[INFO] processing image 3165/9955
[INFO] processing image 3166/9955
[INFO] processing image 3167/9955
[INFO] processing image 3168/9955
[INFO] processing image 3169/9955
[INFO] processing image 3170/9955
[INFO] processing image 3171/9955
[INFO] processing image 3172/9955
[INFO] processing image 3173/9955
[INFO] processing image 3174/9955
[INFO] processing image 3175/9955
[INFO] processing image 3176/9955
[INFO] processing image 3177/9955
[INFO] processing image 3178/9955
[INFO] processing image 3179/9955
[INFO] processing image 3180/9955
[INFO] processing image 3181/9955
[INFO] processing image 3182/9955
[INFO] processing image 3183/9955
[INFO] processing image 3184/9955
[INFO] processing image 3185/9955
[INFO] processing image 3186/9955
[INFO] processing image 3187/9955
[INFO] processing image 3188/9955
[INFO] processing image 3189/9955
[INFO] processing image 3190/9955
[INFO] processing image 3191/9955
[INFO] processing image 3192/9955
[INFO] processing image 3193/9955
[INFO] processing image 3194/9955
[INFO] processing image 3195/9955
[INFO] processing image 3196/9955
[INFO] processing image 3197/9955
[INFO] processing image 3198/9955
[INFO] processing image 3199/9955
[INFO] processing image 3200/9955
[INFO] processing image 3201/9955
[INFO] processing image 3202/9955
[INFO] processing image 3203/9955
[INFO] processing image 3204/9955
[INFO] processing image 3205/9955
[INFO] processing image 3206/9955
[INFO] processing image 3207/9955
[INFO] processing image 3208/9955
[INFO] processing image 3209/9955
[INFO] processing image 3210/9955
[INFO] processing image 3211/9955
[INFO] processing image 3212/9955
[INFO] processing image 3213/9955
[INFO] processing image 3214/9955
[INFO] processing image 3215/9955
[INFO] processing image 3216/9955
[INFO] processing image 3217/9955
[INFO] processing image 3218/9955
[INFO] processing image 3219/9955
[INFO] processing image 3220/9955
[INFO] processing image 3221/9955
[INFO] processing image 3222/9955
[INFO] processing image 3223/9955
[INFO] processing image 3224/9955
[INFO] processing image 3225/9955
[INFO] processing image 3226/9955
[INFO] processing image 3227/9955
[INFO] processing image 3228/9955
[INFO] processing image 3229/9955
[INFO] processing image 3230/9955
[INFO] processing image 3231/9955
[INFO] processing image 3232/9955
[INFO] processing image 3233/9955
[INFO] processing image 3234/9955
[INFO] processing image 3235/9955
[INFO] processing image 3236/9955
[INFO] processing image 3237/9955
[INFO] processing image 3238/9955
[INFO] processing image 3239/9955
[INFO] processing image 3240/9955
[INFO] processing image 3241/9955
[INFO] processing image 3242/9955
[INFO] processing image 3243/9955
[INFO] processing image 3244/9955
[INFO] processing image 3245/9955
[INFO] processing image 3246/9955
[INFO] processing image 3247/9955
[INFO] processing image 3248/9955
[INFO] processing image 3249/9955
[INFO] processing image 3250/9955
[INFO] processing image 3251/9955
[INFO] processing image 3252/9955
[INFO] processing image 3253/9955
[INFO] processing image 3254/9955
[INFO] processing image 3255/9955
[INFO] processing image 3256/9955
[INFO] processing image 3257/9955
[INFO] processing image 3258/9955
[INFO] processing image 3259/9955
[INFO] processing image 3260/9955
[INFO] processing image 3261/9955
[INFO] processing image 3262/9955
[INFO] processing image 3263/9955
[INFO] processing image 3264/9955
[INFO] processing image 3265/9955
[INFO] processing image 3266/9955
[INFO] processing image 3267/9955
[INFO] processing image 3268/9955
[INFO] processing image 3269/9955
[INFO] processing image 3270/9955
[INFO] processing image 3271/9955
[INFO] processing image 3272/9955
[INFO] processing image 3273/9955
[INFO] processing image 3274/9955
[INFO] processing image 3275/9955
[INFO] processing image 3276/9955
[INFO] processing image 3277/9955
[INFO] processing image 3278/9955
[INFO] processing image 3279/9955
[INFO] processing image 3280/9955
[INFO] processing image 3281/9955
[INFO] processing image 3282/9955
[INFO] processing image 3283/9955
[INFO] processing image 3284/9955
[INFO] processing image 3285/9955
[INFO] processing image 3286/9955
[INFO] processing image 3287/9955
[INFO] processing image 3288/9955
[INFO] processing image 3289/9955
[INFO] processing image 3290/9955
[INFO] processing image 3291/9955
[INFO] processing image 3292/9955
[INFO] processing image 3293/9955
[INFO] processing image 3294/9955
[INFO] processing image 3295/9955
[INFO] processing image 3296/9955
[INFO] processing image 3297/9955
[INFO] processing image 3298/9955
[INFO] processing image 3299/9955
[INFO] processing image 3300/9955
[INFO] processing image 3301/9955
[INFO] processing image 3302/9955
[INFO] processing image 3303/9955
[INFO] processing image 3304/9955
[INFO] processing image 3305/9955
[INFO] processing image 3306/9955
[INFO] processing image 3307/9955
[INFO] processing image 3308/9955
[INFO] processing image 3309/9955
[INFO] processing image 3310/9955
[INFO] processing image 3311/9955
[INFO] processing image 3312/9955
[INFO] processing image 3313/9955
[INFO] processing image 3314/9955
[INFO] processing image 3315/9955
[INFO] processing image 3316/9955
[INFO] processing image 3317/9955
[INFO] processing image 3318/9955
[INFO] processing image 3319/9955
[INFO] processing image 3320/9955
[INFO] processing image 3321/9955
[INFO] processing image 3322/9955
[INFO] processing image 3323/9955
[INFO] processing image 3324/9955
[INFO] processing image 3325/9955
[INFO] processing image 3326/9955
[INFO] processing image 3327/9955
[INFO] processing image 3328/9955
[INFO] processing image 3329/9955
[INFO] processing image 3330/9955
[INFO] processing image 3331/9955
[INFO] processing image 3332/9955
[INFO] processing image 3333/9955
[INFO] processing image 3334/9955
[INFO] processing image 3335/9955
[INFO] processing image 3336/9955
[INFO] processing image 3337/9955
[INFO] processing image 3338/9955
[INFO] processing image 3339/9955
[INFO] processing image 3340/9955
[INFO] processing image 3341/9955
[INFO] processing image 3342/9955
[INFO] processing image 3343/9955
[INFO] processing image 3344/9955
[INFO] processing image 3345/9955
[INFO] processing image 3346/9955
[INFO] processing image 3347/9955
[INFO] processing image 3348/9955
[INFO] processing image 3349/9955
[INFO] processing image 3350/9955
[INFO] processing image 3351/9955
[INFO] processing image 3352/9955
[INFO] processing image 3353/9955
[INFO] processing image 3354/9955
[INFO] processing image 3355/9955
[INFO] processing image 3356/9955
[INFO] processing image 3357/9955
[INFO] processing image 3358/9955
[INFO] processing image 3359/9955
[INFO] processing image 3360/9955
[INFO] processing image 3361/9955
[INFO] processing image 3362/9955
[INFO] processing image 3363/9955
[INFO] processing image 3364/9955
[INFO] processing image 3365/9955
[INFO] processing image 3366/9955
[INFO] processing image 3367/9955
[INFO] processing image 3368/9955
[INFO] processing image 3369/9955
[INFO] processing image 3370/9955
[INFO] processing image 3371/9955
[INFO] processing image 3372/9955
[INFO] processing image 3373/9955
[INFO] processing image 3374/9955
[INFO] processing image 3375/9955
[INFO] processing image 3376/9955
[INFO] processing image 3377/9955
[INFO] processing image 3378/9955
[INFO] processing image 3379/9955
[INFO] processing image 3380/9955
[INFO] processing image 3381/9955
[INFO] processing image 3382/9955
[INFO] processing image 3383/9955
[INFO] processing image 3384/9955
[INFO] processing image 3385/9955
[INFO] processing image 3386/9955
[INFO] processing image 3387/9955
[INFO] processing image 3388/9955
[INFO] processing image 3389/9955
[INFO] processing image 3390/9955
[INFO] processing image 3391/9955
[INFO] processing image 3392/9955
[INFO] processing image 3393/9955
[INFO] processing image 3394/9955
[INFO] processing image 3395/9955
[INFO] processing image 3396/9955
[INFO] processing image 3397/9955
[INFO] processing image 3398/9955
[INFO] processing image 3399/9955
[INFO] processing image 3400/9955
[INFO] processing image 3401/9955
[INFO] processing image 3402/9955
[INFO] processing image 3403/9955
[INFO] processing image 3404/9955
[INFO] processing image 3405/9955
[INFO] processing image 3406/9955
[INFO] processing image 3407/9955
[INFO] processing image 3408/9955
[INFO] processing image 3409/9955
[INFO] processing image 3410/9955
[INFO] processing image 3411/9955
[INFO] processing image 3412/9955
[INFO] processing image 3413/9955
[INFO] processing image 3414/9955
[INFO] processing image 3415/9955
[INFO] processing image 3416/9955
[INFO] processing image 3417/9955
[INFO] processing image 3418/9955
[INFO] processing image 3419/9955
[INFO] processing image 3420/9955
[INFO] processing image 3421/9955
[INFO] processing image 3422/9955
[INFO] processing image 3423/9955
[INFO] processing image 3424/9955
[INFO] processing image 3425/9955
[INFO] processing image 3426/9955
[INFO] processing image 3427/9955
[INFO] processing image 3428/9955
[INFO] processing image 3429/9955
[INFO] processing image 3430/9955
[INFO] processing image 3431/9955
[INFO] processing image 3432/9955
[INFO] processing image 3433/9955
[INFO] processing image 3434/9955
[INFO] processing image 3435/9955
[INFO] processing image 3436/9955
[INFO] processing image 3437/9955
[INFO] processing image 3438/9955
[INFO] processing image 3439/9955
[INFO] processing image 3440/9955
[INFO] processing image 3441/9955
[INFO] processing image 3442/9955
[INFO] processing image 3443/9955
[INFO] processing image 3444/9955
[INFO] processing image 3445/9955
[INFO] processing image 3446/9955
[INFO] processing image 3447/9955
[INFO] processing image 3448/9955
[INFO] processing image 3449/9955
[INFO] processing image 3450/9955
[INFO] processing image 3451/9955
[INFO] processing image 3452/9955
[INFO] processing image 3453/9955
[INFO] processing image 3454/9955
[INFO] processing image 3455/9955
[INFO] processing image 3456/9955
[INFO] processing image 3457/9955
[INFO] processing image 3458/9955
[INFO] processing image 3459/9955
[INFO] processing image 3460/9955
[INFO] processing image 3461/9955
[INFO] processing image 3462/9955
[INFO] processing image 3463/9955
[INFO] processing image 3464/9955
[INFO] processing image 3465/9955
[INFO] processing image 3466/9955
[INFO] processing image 3467/9955
[INFO] processing image 3468/9955
[INFO] processing image 3469/9955
[INFO] processing image 3470/9955
[INFO] processing image 3471/9955
[INFO] processing image 3472/9955
[INFO] processing image 3473/9955
[INFO] processing image 3474/9955
[INFO] processing image 3475/9955
[INFO] processing image 3476/9955
[INFO] processing image 3477/9955
[INFO] processing image 3478/9955
[INFO] processing image 3479/9955
[INFO] processing image 3480/9955
[INFO] processing image 3481/9955
[INFO] processing image 3482/9955
[INFO] processing image 3483/9955
[INFO] processing image 3484/9955
[INFO] processing image 3485/9955
[INFO] processing image 3486/9955
[INFO] processing image 3487/9955
[INFO] processing image 3488/9955
[INFO] processing image 3489/9955
[INFO] processing image 3490/9955
[INFO] processing image 3491/9955
[INFO] processing image 3492/9955
[INFO] processing image 3493/9955
[INFO] processing image 3494/9955
[INFO] processing image 3495/9955
[INFO] processing image 3496/9955
[INFO] processing image 3497/9955
[INFO] processing image 3498/9955
[INFO] processing image 3499/9955
[INFO] processing image 3500/9955
[INFO] processing image 3501/9955
[INFO] processing image 3502/9955
[INFO] processing image 3503/9955
[INFO] processing image 3504/9955
[INFO] processing image 3505/9955
[INFO] processing image 3506/9955
[INFO] processing image 3507/9955
[INFO] processing image 3508/9955
[INFO] processing image 3509/9955
[INFO] processing image 3510/9955
[INFO] processing image 3511/9955
[INFO] processing image 3512/9955
[INFO] processing image 3513/9955
[INFO] processing image 3514/9955
[INFO] processing image 3515/9955
[INFO] processing image 3516/9955
[INFO] processing image 3517/9955
[INFO] processing image 3518/9955
[INFO] processing image 3519/9955
[INFO] processing image 3520/9955
[INFO] processing image 3521/9955
[INFO] processing image 3522/9955
[INFO] processing image 3523/9955
[INFO] processing image 3524/9955
[INFO] processing image 3525/9955
[INFO] processing image 3526/9955
[INFO] processing image 3527/9955
[INFO] processing image 3528/9955
[INFO] processing image 3529/9955
[INFO] processing image 3530/9955
[INFO] processing image 3531/9955
[INFO] processing image 3532/9955
[INFO] processing image 3533/9955
[INFO] processing image 3534/9955
[INFO] processing image 3535/9955
[INFO] processing image 3536/9955
[INFO] processing image 3537/9955
[INFO] processing image 3538/9955
[INFO] processing image 3539/9955
[INFO] processing image 3540/9955
[INFO] processing image 3541/9955
[INFO] processing image 3542/9955
[INFO] processing image 3543/9955
[INFO] processing image 3544/9955
[INFO] processing image 3545/9955
[INFO] processing image 3546/9955
[INFO] processing image 3547/9955
[INFO] processing image 3548/9955
[INFO] processing image 3549/9955
[INFO] processing image 3550/9955
[INFO] processing image 3551/9955
[INFO] processing image 3552/9955
[INFO] processing image 3553/9955
[INFO] processing image 3554/9955
[INFO] processing image 3555/9955
[INFO] processing image 3556/9955
[INFO] processing image 3557/9955
[INFO] processing image 3558/9955
[INFO] processing image 3559/9955
[INFO] processing image 3560/9955
[INFO] processing image 3561/9955
[INFO] processing image 3562/9955
[INFO] processing image 3563/9955
[INFO] processing image 3564/9955
[INFO] processing image 3565/9955
[INFO] processing image 3566/9955
[INFO] processing image 3567/9955
[INFO] processing image 3568/9955
[INFO] processing image 3569/9955
[INFO] processing image 3570/9955
[INFO] processing image 3571/9955
[INFO] processing image 3572/9955
[INFO] processing image 3573/9955
[INFO] processing image 3574/9955
[INFO] processing image 3575/9955
[INFO] processing image 3576/9955
[INFO] processing image 3577/9955
[INFO] processing image 3578/9955
[INFO] processing image 3579/9955
[INFO] processing image 3580/9955
[INFO] processing image 3581/9955
[INFO] processing image 3582/9955
[INFO] processing image 3583/9955
[INFO] processing image 3584/9955
[INFO] processing image 3585/9955
[INFO] processing image 3586/9955
[INFO] processing image 3587/9955
[INFO] processing image 3588/9955
[INFO] processing image 3589/9955
[INFO] processing image 3590/9955
[INFO] processing image 3591/9955
[INFO] processing image 3592/9955
[INFO] processing image 3593/9955
[INFO] processing image 3594/9955
[INFO] processing image 3595/9955
[INFO] processing image 3596/9955
[INFO] processing image 3597/9955
[INFO] processing image 3598/9955
[INFO] processing image 3599/9955
[INFO] processing image 3600/9955
[INFO] processing image 3601/9955
[INFO] processing image 3602/9955
[INFO] processing image 3603/9955
[INFO] processing image 3604/9955
[INFO] processing image 3605/9955
[INFO] processing image 3606/9955
[INFO] processing image 3607/9955
[INFO] processing image 3608/9955
[INFO] processing image 3609/9955
[INFO] processing image 3610/9955
[INFO] processing image 3611/9955
[INFO] processing image 3612/9955
[INFO] processing image 3613/9955
[INFO] processing image 3614/9955
[INFO] processing image 3615/9955
[INFO] processing image 3616/9955
[INFO] processing image 3617/9955
[INFO] processing image 3618/9955
[INFO] processing image 3619/9955
[INFO] processing image 3620/9955
[INFO] processing image 3621/9955
[INFO] processing image 3622/9955
[INFO] processing image 3623/9955
[INFO] processing image 3624/9955
[INFO] processing image 3625/9955
[INFO] processing image 3626/9955
[INFO] processing image 3627/9955
[INFO] processing image 3628/9955
[INFO] processing image 3629/9955
[INFO] processing image 3630/9955
[INFO] processing image 3631/9955
[INFO] processing image 3632/9955
[INFO] processing image 3633/9955
[INFO] processing image 3634/9955
[INFO] processing image 3635/9955
[INFO] processing image 3636/9955
[INFO] processing image 3637/9955
[INFO] processing image 3638/9955
[INFO] processing image 3639/9955
[INFO] processing image 3640/9955
[INFO] processing image 3641/9955
[INFO] processing image 3642/9955
[INFO] processing image 3643/9955
[INFO] processing image 3644/9955
[INFO] processing image 3645/9955
[INFO] processing image 3646/9955
[INFO] processing image 3647/9955
[INFO] processing image 3648/9955
[INFO] processing image 3649/9955
[INFO] processing image 3650/9955
[INFO] processing image 3651/9955
[INFO] processing image 3652/9955
[INFO] processing image 3653/9955
[INFO] processing image 3654/9955
[INFO] processing image 3655/9955
[INFO] processing image 3656/9955
[INFO] processing image 3657/9955
[INFO] processing image 3658/9955
[INFO] processing image 3659/9955
[INFO] processing image 3660/9955
[INFO] processing image 3661/9955
[INFO] processing image 3662/9955
[INFO] processing image 3663/9955
[INFO] processing image 3664/9955
[INFO] processing image 3665/9955
[INFO] processing image 3666/9955
[INFO] processing image 3667/9955
[INFO] processing image 3668/9955
[INFO] processing image 3669/9955
[INFO] processing image 3670/9955
[INFO] processing image 3671/9955
[INFO] processing image 3672/9955
[INFO] processing image 3673/9955
[INFO] processing image 3674/9955
[INFO] processing image 3675/9955
[INFO] processing image 3676/9955
[INFO] processing image 3677/9955
[INFO] processing image 3678/9955
[INFO] processing image 3679/9955
[INFO] processing image 3680/9955
[INFO] processing image 3681/9955
[INFO] processing image 3682/9955
[INFO] processing image 3683/9955
[INFO] processing image 3684/9955
[INFO] processing image 3685/9955
[INFO] processing image 3686/9955
[INFO] processing image 3687/9955
[INFO] processing image 3688/9955
[INFO] processing image 3689/9955
[INFO] processing image 3690/9955
[INFO] processing image 3691/9955
[INFO] processing image 3692/9955
[INFO] processing image 3693/9955
[INFO] processing image 3694/9955
[INFO] processing image 3695/9955
[INFO] processing image 3696/9955
[INFO] processing image 3697/9955
[INFO] processing image 3698/9955
[INFO] processing image 3699/9955
[INFO] processing image 3700/9955
[INFO] processing image 3701/9955
[INFO] processing image 3702/9955
[INFO] processing image 3703/9955
[INFO] processing image 3704/9955
[INFO] processing image 3705/9955
[INFO] processing image 3706/9955
[INFO] processing image 3707/9955
[INFO] processing image 3708/9955
[INFO] processing image 3709/9955
[INFO] processing image 3710/9955
[INFO] processing image 3711/9955
[INFO] processing image 3712/9955
[INFO] processing image 3713/9955
[INFO] processing image 3714/9955
[INFO] processing image 3715/9955
[INFO] processing image 3716/9955
[INFO] processing image 3717/9955
[INFO] processing image 3718/9955
[INFO] processing image 3719/9955
[INFO] processing image 3720/9955
[INFO] processing image 3721/9955
[INFO] processing image 3722/9955
[INFO] processing image 3723/9955
[INFO] processing image 3724/9955
[INFO] processing image 3725/9955
[INFO] processing image 3726/9955
[INFO] processing image 3727/9955
[INFO] processing image 3728/9955
[INFO] processing image 3729/9955
[INFO] processing image 3730/9955
[INFO] processing image 3731/9955
[INFO] processing image 3732/9955
[INFO] processing image 3733/9955
[INFO] processing image 3734/9955
[INFO] processing image 3735/9955
[INFO] processing image 3736/9955
[INFO] processing image 3737/9955
[INFO] processing image 3738/9955
[INFO] processing image 3739/9955
[INFO] processing image 3740/9955
[INFO] processing image 3741/9955
[INFO] processing image 3742/9955
[INFO] processing image 3743/9955
[INFO] processing image 3744/9955
[INFO] processing image 3745/9955
[INFO] processing image 3746/9955
[INFO] processing image 3747/9955
[INFO] processing image 3748/9955
[INFO] processing image 3749/9955
[INFO] processing image 3750/9955
[INFO] processing image 3751/9955
[INFO] processing image 3752/9955
[INFO] processing image 3753/9955
[INFO] processing image 3754/9955
[INFO] processing image 3755/9955
[INFO] processing image 3756/9955
[INFO] processing image 3757/9955
[INFO] processing image 3758/9955
[INFO] processing image 3759/9955
[INFO] processing image 3760/9955
[INFO] processing image 3761/9955
[INFO] processing image 3762/9955
[INFO] processing image 3763/9955
[INFO] processing image 3764/9955
[INFO] processing image 3765/9955
[INFO] processing image 3766/9955
[INFO] processing image 3767/9955
[INFO] processing image 3768/9955
[INFO] processing image 3769/9955
[INFO] processing image 3770/9955
[INFO] processing image 3771/9955
[INFO] processing image 3772/9955
[INFO] processing image 3773/9955
[INFO] processing image 3774/9955
[INFO] processing image 3775/9955
[INFO] processing image 3776/9955
[INFO] processing image 3777/9955
[INFO] processing image 3778/9955
[INFO] processing image 3779/9955
[INFO] processing image 3780/9955
[INFO] processing image 3781/9955
[INFO] processing image 3782/9955
[INFO] processing image 3783/9955
[INFO] processing image 3784/9955
[INFO] processing image 3785/9955
[INFO] processing image 3786/9955
[INFO] processing image 3787/9955
[INFO] processing image 3788/9955
[INFO] processing image 3789/9955
[INFO] processing image 3790/9955
[INFO] processing image 3791/9955
[INFO] processing image 3792/9955
[INFO] processing image 3793/9955
[INFO] processing image 3794/9955
[INFO] processing image 3795/9955
[INFO] processing image 3796/9955
[INFO] processing image 3797/9955
[INFO] processing image 3798/9955
[INFO] processing image 3799/9955
[INFO] processing image 3800/9955
[INFO] processing image 3801/9955
[INFO] processing image 3802/9955
[INFO] processing image 3803/9955
[INFO] processing image 3804/9955
[INFO] processing image 3805/9955
[INFO] processing image 3806/9955
[INFO] processing image 3807/9955
[INFO] processing image 3808/9955
[INFO] processing image 3809/9955
[INFO] processing image 3810/9955
[INFO] processing image 3811/9955
[INFO] processing image 3812/9955
[INFO] processing image 3813/9955
[INFO] processing image 3814/9955
[INFO] processing image 3815/9955
[INFO] processing image 3816/9955
[INFO] processing image 3817/9955
[INFO] processing image 3818/9955
[INFO] processing image 3819/9955
[INFO] processing image 3820/9955
[INFO] processing image 3821/9955
[INFO] processing image 3822/9955
[INFO] processing image 3823/9955
[INFO] processing image 3824/9955
[INFO] processing image 3825/9955
[INFO] processing image 3826/9955
[INFO] processing image 3827/9955
[INFO] processing image 3828/9955
[INFO] processing image 3829/9955
[INFO] processing image 3830/9955
[INFO] processing image 3831/9955
[INFO] processing image 3832/9955
[INFO] processing image 3833/9955
[INFO] processing image 3834/9955
[INFO] processing image 3835/9955
[INFO] processing image 3836/9955
[INFO] processing image 3837/9955
[INFO] processing image 3838/9955
[INFO] processing image 3839/9955
[INFO] processing image 3840/9955
[INFO] processing image 3841/9955
[INFO] processing image 3842/9955
[INFO] processing image 3843/9955
[INFO] processing image 3844/9955
[INFO] processing image 3845/9955
[INFO] processing image 3846/9955
[INFO] processing image 3847/9955
[INFO] processing image 3848/9955
[INFO] processing image 3849/9955
[INFO] processing image 3850/9955
[INFO] processing image 3851/9955
[INFO] processing image 3852/9955
[INFO] processing image 3853/9955
[INFO] processing image 3854/9955
[INFO] processing image 3855/9955
[INFO] processing image 3856/9955
[INFO] processing image 3857/9955
[INFO] processing image 3858/9955
[INFO] processing image 3859/9955
[INFO] processing image 3860/9955
[INFO] processing image 3861/9955
[INFO] processing image 3862/9955
[INFO] processing image 3863/9955
[INFO] processing image 3864/9955
[INFO] processing image 3865/9955
[INFO] processing image 3866/9955
[INFO] processing image 3867/9955
[INFO] processing image 3868/9955
[INFO] processing image 3869/9955
[INFO] processing image 3870/9955
[INFO] processing image 3871/9955
[INFO] processing image 3872/9955
[INFO] processing image 3873/9955
[INFO] processing image 3874/9955
[INFO] processing image 3875/9955
[INFO] processing image 3876/9955
[INFO] processing image 3877/9955
[INFO] processing image 3878/9955
[INFO] processing image 3879/9955
[INFO] processing image 3880/9955
[INFO] processing image 3881/9955
[INFO] processing image 3882/9955
[INFO] processing image 3883/9955
[INFO] processing image 3884/9955
[INFO] processing image 3885/9955
[INFO] processing image 3886/9955
[INFO] processing image 3887/9955
[INFO] processing image 3888/9955
[INFO] processing image 3889/9955
[INFO] processing image 3890/9955
[INFO] processing image 3891/9955
[INFO] processing image 3892/9955
[INFO] processing image 3893/9955
[INFO] processing image 3894/9955
[INFO] processing image 3895/9955
[INFO] processing image 3896/9955
[INFO] processing image 3897/9955
[INFO] processing image 3898/9955
[INFO] processing image 3899/9955
[INFO] processing image 3900/9955
[INFO] processing image 3901/9955
[INFO] processing image 3902/9955
[INFO] processing image 3903/9955
[INFO] processing image 3904/9955
[INFO] processing image 3905/9955
[INFO] processing image 3906/9955
[INFO] processing image 3907/9955
[INFO] processing image 3908/9955
[INFO] processing image 3909/9955
[INFO] processing image 3910/9955
[INFO] processing image 3911/9955
[INFO] processing image 3912/9955
[INFO] processing image 3913/9955
[INFO] processing image 3914/9955
[INFO] processing image 3915/9955
[INFO] processing image 3916/9955
[INFO] processing image 3917/9955
[INFO] processing image 3918/9955
[INFO] processing image 3919/9955
[INFO] processing image 3920/9955
[INFO] processing image 3921/9955
[INFO] processing image 3922/9955
[INFO] processing image 3923/9955
[INFO] processing image 3924/9955
[INFO] processing image 3925/9955
[INFO] processing image 3926/9955
[INFO] processing image 3927/9955
[INFO] processing image 3928/9955
[INFO] processing image 3929/9955
[INFO] processing image 3930/9955
[INFO] processing image 3931/9955
[INFO] processing image 3932/9955
[INFO] processing image 3933/9955
[INFO] processing image 3934/9955
[INFO] processing image 3935/9955
[INFO] processing image 3936/9955
[INFO] processing image 3937/9955
[INFO] processing image 3938/9955
[INFO] processing image 3939/9955
[INFO] processing image 3940/9955
[INFO] processing image 3941/9955
[INFO] processing image 3942/9955
[INFO] processing image 3943/9955
[INFO] processing image 3944/9955
[INFO] processing image 3945/9955
[INFO] processing image 3946/9955
[INFO] processing image 3947/9955
[INFO] processing image 3948/9955
[INFO] processing image 3949/9955
[INFO] processing image 3950/9955
[INFO] processing image 3951/9955
[INFO] processing image 3952/9955
[INFO] processing image 3953/9955
[INFO] processing image 3954/9955
[INFO] processing image 3955/9955
[INFO] processing image 3956/9955
[INFO] processing image 3957/9955
[INFO] processing image 3958/9955
[INFO] processing image 3959/9955
[INFO] processing image 3960/9955
[INFO] processing image 3961/9955
[INFO] processing image 3962/9955
[INFO] processing image 3963/9955
[INFO] processing image 3964/9955
[INFO] processing image 3965/9955
[INFO] processing image 3966/9955
[INFO] processing image 3967/9955
[INFO] processing image 3968/9955
[INFO] processing image 3969/9955
[INFO] processing image 3970/9955
[INFO] processing image 3971/9955
[INFO] processing image 3972/9955
[INFO] processing image 3973/9955
[INFO] processing image 3974/9955
[INFO] processing image 3975/9955
[INFO] processing image 3976/9955
[INFO] processing image 3977/9955
[INFO] processing image 3978/9955
[INFO] processing image 3979/9955
[INFO] processing image 3980/9955
[INFO] processing image 3981/9955
[INFO] processing image 3982/9955
[INFO] processing image 3983/9955
[INFO] processing image 3984/9955
[INFO] processing image 3985/9955
[INFO] processing image 3986/9955
[INFO] processing image 3987/9955
[INFO] processing image 3988/9955
[INFO] processing image 3989/9955
[INFO] processing image 3990/9955
[INFO] processing image 3991/9955
[INFO] processing image 3992/9955
[INFO] processing image 3993/9955
[INFO] processing image 3994/9955
[INFO] processing image 3995/9955
[INFO] processing image 3996/9955
[INFO] processing image 3997/9955
[INFO] processing image 3998/9955
[INFO] processing image 3999/9955
[INFO] processing image 4000/9955
[INFO] processing image 4001/9955
[INFO] processing image 4002/9955
[INFO] processing image 4003/9955
[INFO] processing image 4004/9955
[INFO] processing image 4005/9955
[INFO] processing image 4006/9955
[INFO] processing image 4007/9955
[INFO] processing image 4008/9955
[INFO] processing image 4009/9955
[INFO] processing image 4010/9955
[INFO] processing image 4011/9955
[INFO] processing image 4012/9955
[INFO] processing image 4013/9955
[INFO] processing image 4014/9955
[INFO] processing image 4015/9955
[INFO] processing image 4016/9955
[INFO] processing image 4017/9955
[INFO] processing image 4018/9955
[INFO] processing image 4019/9955
[INFO] processing image 4020/9955
[INFO] processing image 4021/9955
[INFO] processing image 4022/9955
[INFO] processing image 4023/9955
[INFO] processing image 4024/9955
[INFO] processing image 4025/9955
[INFO] processing image 4026/9955
[INFO] processing image 4027/9955
[INFO] processing image 4028/9955
[INFO] processing image 4029/9955
[INFO] processing image 4030/9955
[INFO] processing image 4031/9955
[INFO] processing image 4032/9955
[INFO] processing image 4033/9955
[INFO] processing image 4034/9955
[INFO] processing image 4035/9955
[INFO] processing image 4036/9955
[INFO] processing image 4037/9955
[INFO] processing image 4038/9955
[INFO] processing image 4039/9955
[INFO] processing image 4040/9955
[INFO] processing image 4041/9955
[INFO] processing image 4042/9955
[INFO] processing image 4043/9955
[INFO] processing image 4044/9955
[INFO] processing image 4045/9955
[INFO] processing image 4046/9955
[INFO] processing image 4047/9955
[INFO] processing image 4048/9955
[INFO] processing image 4049/9955
[INFO] processing image 4050/9955
[INFO] processing image 4051/9955
[INFO] processing image 4052/9955
[INFO] processing image 4053/9955
[INFO] processing image 4054/9955
[INFO] processing image 4055/9955
[INFO] processing image 4056/9955
[INFO] processing image 4057/9955
[INFO] processing image 4058/9955
[INFO] processing image 4059/9955
[INFO] processing image 4060/9955
[INFO] processing image 4061/9955
[INFO] processing image 4062/9955
[INFO] processing image 4063/9955
[INFO] processing image 4064/9955
[INFO] processing image 4065/9955
[INFO] processing image 4066/9955
[INFO] processing image 4067/9955
[INFO] processing image 4068/9955
[INFO] processing image 4069/9955
[INFO] processing image 4070/9955
[INFO] processing image 4071/9955
[INFO] processing image 4072/9955
[INFO] processing image 4073/9955
[INFO] processing image 4074/9955
[INFO] processing image 4075/9955
[INFO] processing image 4076/9955
[INFO] processing image 4077/9955
[INFO] processing image 4078/9955
[INFO] processing image 4079/9955
[INFO] processing image 4080/9955
[INFO] processing image 4081/9955
[INFO] processing image 4082/9955
[INFO] processing image 4083/9955
[INFO] processing image 4084/9955
[INFO] processing image 4085/9955
[INFO] processing image 4086/9955
[INFO] processing image 4087/9955
[INFO] processing image 4088/9955
[INFO] processing image 4089/9955
[INFO] processing image 4090/9955
[INFO] processing image 4091/9955
[INFO] processing image 4092/9955
[INFO] processing image 4093/9955
[INFO] processing image 4094/9955
[INFO] processing image 4095/9955
[INFO] processing image 4096/9955
[INFO] processing image 4097/9955
[INFO] processing image 4098/9955
[INFO] processing image 4099/9955
[INFO] processing image 4100/9955
[INFO] processing image 4101/9955
[INFO] processing image 4102/9955
[INFO] processing image 4103/9955
[INFO] processing image 4104/9955
[INFO] processing image 4105/9955
[INFO] processing image 4106/9955
[INFO] processing image 4107/9955
[INFO] processing image 4108/9955
[INFO] processing image 4109/9955
[INFO] processing image 4110/9955
[INFO] processing image 4111/9955
[INFO] processing image 4112/9955
[INFO] processing image 4113/9955
[INFO] processing image 4114/9955
[INFO] processing image 4115/9955
[INFO] processing image 4116/9955
[INFO] processing image 4117/9955
[INFO] processing image 4118/9955
[INFO] processing image 4119/9955
[INFO] processing image 4120/9955
[INFO] processing image 4121/9955
[INFO] processing image 4122/9955
[INFO] processing image 4123/9955
[INFO] processing image 4124/9955
[INFO] processing image 4125/9955
[INFO] processing image 4126/9955
[INFO] processing image 4127/9955
[INFO] processing image 4128/9955
[INFO] processing image 4129/9955
[INFO] processing image 4130/9955
[INFO] processing image 4131/9955
[INFO] processing image 4132/9955
[INFO] processing image 4133/9955
[INFO] processing image 4134/9955
[INFO] processing image 4135/9955
[INFO] processing image 4136/9955
[INFO] processing image 4137/9955
[INFO] processing image 4138/9955
[INFO] processing image 4139/9955
[INFO] processing image 4140/9955
[INFO] processing image 4141/9955
[INFO] processing image 4142/9955
[INFO] processing image 4143/9955
[INFO] processing image 4144/9955
[INFO] processing image 4145/9955
[INFO] processing image 4146/9955
[INFO] processing image 4147/9955
[INFO] processing image 4148/9955
[INFO] processing image 4149/9955
[INFO] processing image 4150/9955
[INFO] processing image 4151/9955
[INFO] processing image 4152/9955
[INFO] processing image 4153/9955
[INFO] processing image 4154/9955
[INFO] processing image 4155/9955
[INFO] processing image 4156/9955
[INFO] processing image 4157/9955
[INFO] processing image 4158/9955
[INFO] processing image 4159/9955
[INFO] processing image 4160/9955
[INFO] processing image 4161/9955
[INFO] processing image 4162/9955
[INFO] processing image 4163/9955
[INFO] processing image 4164/9955
[INFO] processing image 4165/9955
[INFO] processing image 4166/9955
[INFO] processing image 4167/9955
[INFO] processing image 4168/9955
[INFO] processing image 4169/9955
[INFO] processing image 4170/9955
[INFO] processing image 4171/9955
[INFO] processing image 4172/9955
[INFO] processing image 4173/9955
[INFO] processing image 4174/9955
[INFO] processing image 4175/9955
[INFO] processing image 4176/9955
[INFO] processing image 4177/9955
[INFO] processing image 4178/9955
[INFO] processing image 4179/9955
[INFO] processing image 4180/9955
[INFO] processing image 4181/9955
[INFO] processing image 4182/9955
[INFO] processing image 4183/9955
[INFO] processing image 4184/9955
[INFO] processing image 4185/9955
[INFO] processing image 4186/9955
[INFO] processing image 4187/9955
[INFO] processing image 4188/9955
[INFO] processing image 4189/9955
[INFO] processing image 4190/9955
[INFO] processing image 4191/9955
[INFO] processing image 4192/9955
[INFO] processing image 4193/9955
[INFO] processing image 4194/9955
[INFO] processing image 4195/9955
[INFO] processing image 4196/9955
[INFO] processing image 4197/9955
[INFO] processing image 4198/9955
[INFO] processing image 4199/9955
[INFO] processing image 4200/9955
[INFO] processing image 4201/9955
[INFO] processing image 4202/9955
[INFO] processing image 4203/9955
[INFO] processing image 4204/9955
[INFO] processing image 4205/9955
[INFO] processing image 4206/9955
[INFO] processing image 4207/9955
[INFO] processing image 4208/9955
[INFO] processing image 4209/9955
[INFO] processing image 4210/9955
[INFO] processing image 4211/9955
[INFO] processing image 4212/9955
[INFO] processing image 4213/9955
[INFO] processing image 4214/9955
[INFO] processing image 4215/9955
[INFO] processing image 4216/9955
[INFO] processing image 4217/9955
[INFO] processing image 4218/9955
[INFO] processing image 4219/9955
[INFO] processing image 4220/9955
[INFO] processing image 4221/9955
[INFO] processing image 4222/9955
[INFO] processing image 4223/9955
[INFO] processing image 4224/9955
[INFO] processing image 4225/9955
[INFO] processing image 4226/9955
[INFO] processing image 4227/9955
[INFO] processing image 4228/9955
[INFO] processing image 4229/9955
[INFO] processing image 4230/9955
[INFO] processing image 4231/9955
[INFO] processing image 4232/9955
[INFO] processing image 4233/9955
[INFO] processing image 4234/9955
[INFO] processing image 4235/9955
[INFO] processing image 4236/9955
[INFO] processing image 4237/9955
[INFO] processing image 4238/9955
[INFO] processing image 4239/9955
[INFO] processing image 4240/9955
[INFO] processing image 4241/9955
[INFO] processing image 4242/9955
[INFO] processing image 4243/9955
[INFO] processing image 4244/9955
[INFO] processing image 4245/9955
[INFO] processing image 4246/9955
[INFO] processing image 4247/9955
[INFO] processing image 4248/9955
[INFO] processing image 4249/9955
[INFO] processing image 4250/9955
[INFO] processing image 4251/9955
[INFO] processing image 4252/9955
[INFO] processing image 4253/9955
[INFO] processing image 4254/9955
[INFO] processing image 4255/9955
[INFO] processing image 4256/9955
[INFO] processing image 4257/9955
[INFO] processing image 4258/9955
[INFO] processing image 4259/9955
[INFO] processing image 4260/9955
[INFO] processing image 4261/9955
[INFO] processing image 4262/9955
[INFO] processing image 4263/9955
[INFO] processing image 4264/9955
[INFO] processing image 4265/9955
[INFO] processing image 4266/9955
[INFO] processing image 4267/9955
[INFO] processing image 4268/9955
[INFO] processing image 4269/9955
[INFO] processing image 4270/9955
[INFO] processing image 4271/9955
[INFO] processing image 4272/9955
[INFO] processing image 4273/9955
[INFO] processing image 4274/9955
[INFO] processing image 4275/9955
[INFO] processing image 4276/9955
[INFO] processing image 4277/9955
[INFO] processing image 4278/9955
[INFO] processing image 4279/9955
[INFO] processing image 4280/9955
[INFO] processing image 4281/9955
[INFO] processing image 4282/9955
[INFO] processing image 4283/9955
[INFO] processing image 4284/9955
[INFO] processing image 4285/9955
[INFO] processing image 4286/9955
[INFO] processing image 4287/9955
[INFO] processing image 4288/9955
[INFO] processing image 4289/9955
[INFO] processing image 4290/9955
[INFO] processing image 4291/9955
[INFO] processing image 4292/9955
[INFO] processing image 4293/9955
[INFO] processing image 4294/9955
[INFO] processing image 4295/9955
[INFO] processing image 4296/9955
[INFO] processing image 4297/9955
[INFO] processing image 4298/9955
[INFO] processing image 4299/9955
[INFO] processing image 4300/9955
[INFO] processing image 4301/9955
[INFO] processing image 4302/9955
[INFO] processing image 4303/9955
[INFO] processing image 4304/9955
[INFO] processing image 4305/9955
[INFO] processing image 4306/9955
[INFO] processing image 4307/9955
[INFO] processing image 4308/9955
[INFO] processing image 4309/9955
[INFO] processing image 4310/9955
[INFO] processing image 4311/9955
[INFO] processing image 4312/9955
[INFO] processing image 4313/9955
[INFO] processing image 4314/9955
[INFO] processing image 4315/9955
[INFO] processing image 4316/9955
[INFO] processing image 4317/9955
[INFO] processing image 4318/9955
[INFO] processing image 4319/9955
[INFO] processing image 4320/9955
[INFO] processing image 4321/9955
[INFO] processing image 4322/9955
[INFO] processing image 4323/9955
[INFO] processing image 4324/9955
[INFO] processing image 4325/9955
[INFO] processing image 4326/9955
[INFO] processing image 4327/9955
[INFO] processing image 4328/9955
[INFO] processing image 4329/9955
[INFO] processing image 4330/9955
[INFO] processing image 4331/9955
[INFO] processing image 4332/9955
[INFO] processing image 4333/9955
[INFO] processing image 4334/9955
[INFO] processing image 4335/9955
[INFO] processing image 4336/9955
[INFO] processing image 4337/9955
[INFO] processing image 4338/9955
[INFO] processing image 4339/9955
[INFO] processing image 4340/9955
[INFO] processing image 4341/9955
[INFO] processing image 4342/9955
[INFO] processing image 4343/9955
[INFO] processing image 4344/9955
[INFO] processing image 4345/9955
[INFO] processing image 4346/9955
[INFO] processing image 4347/9955
[INFO] processing image 4348/9955
[INFO] processing image 4349/9955
[INFO] processing image 4350/9955
[INFO] processing image 4351/9955
[INFO] processing image 4352/9955
[INFO] processing image 4353/9955
[INFO] processing image 4354/9955
[INFO] processing image 4355/9955
[INFO] processing image 4356/9955
[INFO] processing image 4357/9955
[INFO] processing image 4358/9955
[INFO] processing image 4359/9955
[INFO] processing image 4360/9955
[INFO] processing image 4361/9955
[INFO] processing image 4362/9955
[INFO] processing image 4363/9955
[INFO] processing image 4364/9955
[INFO] processing image 4365/9955
[INFO] processing image 4366/9955
[INFO] processing image 4367/9955
[INFO] processing image 4368/9955
[INFO] processing image 4369/9955
[INFO] processing image 4370/9955
[INFO] processing image 4371/9955
[INFO] processing image 4372/9955
[INFO] processing image 4373/9955
[INFO] processing image 4374/9955
[INFO] processing image 4375/9955
[INFO] processing image 4376/9955
[INFO] processing image 4377/9955
[INFO] processing image 4378/9955
[INFO] processing image 4379/9955
[INFO] processing image 4380/9955
[INFO] processing image 4381/9955
[INFO] processing image 4382/9955
[INFO] processing image 4383/9955
[INFO] processing image 4384/9955
[INFO] processing image 4385/9955
[INFO] processing image 4386/9955
[INFO] processing image 4387/9955
[INFO] processing image 4388/9955
[INFO] processing image 4389/9955
[INFO] processing image 4390/9955
[INFO] processing image 4391/9955
[INFO] processing image 4392/9955
[INFO] processing image 4393/9955
[INFO] processing image 4394/9955
[INFO] processing image 4395/9955
[INFO] processing image 4396/9955
[INFO] processing image 4397/9955
[INFO] processing image 4398/9955
[INFO] processing image 4399/9955
[INFO] processing image 4400/9955
[INFO] processing image 4401/9955
[INFO] processing image 4402/9955
[INFO] processing image 4403/9955
[INFO] processing image 4404/9955
[INFO] processing image 4405/9955
[INFO] processing image 4406/9955
[INFO] processing image 4407/9955
[INFO] processing image 4408/9955
[INFO] processing image 4409/9955
[INFO] processing image 4410/9955
[INFO] processing image 4411/9955
[INFO] processing image 4412/9955
[INFO] processing image 4413/9955
[INFO] processing image 4414/9955
[INFO] processing image 4415/9955
[INFO] processing image 4416/9955
[INFO] processing image 4417/9955
[INFO] processing image 4418/9955
[INFO] processing image 4419/9955
[INFO] processing image 4420/9955
[INFO] processing image 4421/9955
[INFO] processing image 4422/9955
[INFO] processing image 4423/9955
[INFO] processing image 4424/9955
[INFO] processing image 4425/9955
[INFO] processing image 4426/9955
[INFO] processing image 4427/9955
[INFO] processing image 4428/9955
[INFO] processing image 4429/9955
[INFO] processing image 4430/9955
[INFO] processing image 4431/9955
[INFO] processing image 4432/9955
[INFO] processing image 4433/9955
[INFO] processing image 4434/9955
[INFO] processing image 4435/9955
[INFO] processing image 4436/9955
[INFO] processing image 4437/9955
[INFO] processing image 4438/9955
[INFO] processing image 4439/9955
[INFO] processing image 4440/9955
[INFO] processing image 4441/9955
[INFO] processing image 4442/9955
[INFO] processing image 4443/9955
[INFO] processing image 4444/9955
[INFO] processing image 4445/9955
[INFO] processing image 4446/9955
[INFO] processing image 4447/9955
[INFO] processing image 4448/9955
[INFO] processing image 4449/9955
[INFO] processing image 4450/9955
[INFO] processing image 4451/9955
[INFO] processing image 4452/9955
[INFO] processing image 4453/9955
[INFO] processing image 4454/9955
[INFO] processing image 4455/9955
[INFO] processing image 4456/9955
[INFO] processing image 4457/9955
[INFO] processing image 4458/9955
[INFO] processing image 4459/9955
[INFO] processing image 4460/9955
[INFO] processing image 4461/9955
[INFO] processing image 4462/9955
[INFO] processing image 4463/9955
[INFO] processing image 4464/9955
[INFO] processing image 4465/9955
[INFO] processing image 4466/9955
[INFO] processing image 4467/9955
[INFO] processing image 4468/9955
[INFO] processing image 4469/9955
[INFO] processing image 4470/9955
[INFO] processing image 4471/9955
[INFO] processing image 4472/9955
[INFO] processing image 4473/9955
[INFO] processing image 4474/9955
[INFO] processing image 4475/9955
[INFO] processing image 4476/9955
[INFO] processing image 4477/9955
[INFO] processing image 4478/9955
[INFO] processing image 4479/9955
[INFO] processing image 4480/9955
[INFO] processing image 4481/9955
[INFO] processing image 4482/9955
[INFO] processing image 4483/9955
[INFO] processing image 4484/9955
[INFO] processing image 4485/9955
[INFO] processing image 4486/9955
[INFO] processing image 4487/9955
[INFO] processing image 4488/9955
[INFO] processing image 4489/9955
[INFO] processing image 4490/9955
[INFO] processing image 4491/9955
[INFO] processing image 4492/9955
[INFO] processing image 4493/9955
[INFO] processing image 4494/9955
[INFO] processing image 4495/9955
[INFO] processing image 4496/9955
[INFO] processing image 4497/9955
[INFO] processing image 4498/9955
[INFO] processing image 4499/9955
[INFO] processing image 4500/9955
[INFO] processing image 4501/9955
[INFO] processing image 4502/9955
[INFO] processing image 4503/9955
[INFO] processing image 4504/9955
[INFO] processing image 4505/9955
[INFO] processing image 4506/9955
[INFO] processing image 4507/9955
[INFO] processing image 4508/9955
[INFO] processing image 4509/9955
[INFO] processing image 4510/9955
[INFO] processing image 4511/9955
[INFO] processing image 4512/9955
[INFO] processing image 4513/9955
[INFO] processing image 4514/9955
[INFO] processing image 4515/9955
[INFO] processing image 4516/9955
[INFO] processing image 4517/9955
[INFO] processing image 4518/9955
[INFO] processing image 4519/9955
[INFO] processing image 4520/9955
[INFO] processing image 4521/9955
[INFO] processing image 4522/9955
[INFO] processing image 4523/9955
[INFO] processing image 4524/9955
[INFO] processing image 4525/9955
[INFO] processing image 4526/9955
[INFO] processing image 4527/9955
[INFO] processing image 4528/9955
[INFO] processing image 4529/9955
[INFO] processing image 4530/9955
[INFO] processing image 4531/9955
[INFO] processing image 4532/9955
[INFO] processing image 4533/9955
[INFO] processing image 4534/9955
[INFO] processing image 4535/9955
[INFO] processing image 4536/9955
[INFO] processing image 4537/9955
[INFO] processing image 4538/9955
[INFO] processing image 4539/9955
[INFO] processing image 4540/9955
[INFO] processing image 4541/9955
[INFO] processing image 4542/9955
[INFO] processing image 4543/9955
[INFO] processing image 4544/9955
[INFO] processing image 4545/9955
[INFO] processing image 4546/9955
[INFO] processing image 4547/9955
[INFO] processing image 4548/9955
[INFO] processing image 4549/9955
[INFO] processing image 4550/9955
[INFO] processing image 4551/9955
[INFO] processing image 4552/9955
[INFO] processing image 4553/9955
[INFO] processing image 4554/9955
[INFO] processing image 4555/9955
[INFO] processing image 4556/9955
[INFO] processing image 4557/9955
[INFO] processing image 4558/9955
[INFO] processing image 4559/9955
[INFO] processing image 4560/9955
[INFO] processing image 4561/9955
[INFO] processing image 4562/9955
[INFO] processing image 4563/9955
[INFO] processing image 4564/9955
[INFO] processing image 4565/9955
[INFO] processing image 4566/9955
[INFO] processing image 4567/9955
[INFO] processing image 4568/9955
[INFO] processing image 4569/9955
[INFO] processing image 4570/9955
[INFO] processing image 4571/9955
[INFO] processing image 4572/9955
[INFO] processing image 4573/9955
[INFO] processing image 4574/9955
[INFO] processing image 4575/9955
[INFO] processing image 4576/9955
[INFO] processing image 4577/9955
[INFO] processing image 4578/9955
[INFO] processing image 4579/9955
[INFO] processing image 4580/9955
[INFO] processing image 4581/9955
[INFO] processing image 4582/9955
[INFO] processing image 4583/9955
[INFO] processing image 4584/9955
[INFO] processing image 4585/9955
[INFO] processing image 4586/9955
[INFO] processing image 4587/9955
[INFO] processing image 4588/9955
[INFO] processing image 4589/9955
[INFO] processing image 4590/9955
[INFO] processing image 4591/9955
[INFO] processing image 4592/9955
[INFO] processing image 4593/9955
[INFO] processing image 4594/9955
[INFO] processing image 4595/9955
[INFO] processing image 4596/9955
[INFO] processing image 4597/9955
[INFO] processing image 4598/9955
[INFO] processing image 4599/9955
[INFO] processing image 4600/9955
[INFO] processing image 4601/9955
[INFO] processing image 4602/9955
[INFO] processing image 4603/9955
[INFO] processing image 4604/9955
[INFO] processing image 4605/9955
[INFO] processing image 4606/9955
[INFO] processing image 4607/9955
[INFO] processing image 4608/9955
[INFO] processing image 4609/9955
[INFO] processing image 4610/9955
[INFO] processing image 4611/9955
[INFO] processing image 4612/9955
[INFO] processing image 4613/9955
[INFO] processing image 4614/9955
[INFO] processing image 4615/9955
[INFO] processing image 4616/9955
[INFO] processing image 4617/9955
[INFO] processing image 4618/9955
[INFO] processing image 4619/9955
[INFO] processing image 4620/9955
[INFO] processing image 4621/9955
[INFO] processing image 4622/9955
[INFO] processing image 4623/9955
[INFO] processing image 4624/9955
[INFO] processing image 4625/9955
[INFO] processing image 4626/9955
[INFO] processing image 4627/9955
[INFO] processing image 4628/9955
[INFO] processing image 4629/9955
[INFO] processing image 4630/9955
[INFO] processing image 4631/9955
[INFO] processing image 4632/9955
[INFO] processing image 4633/9955
[INFO] processing image 4634/9955
[INFO] processing image 4635/9955
[INFO] processing image 4636/9955
[INFO] processing image 4637/9955
[INFO] processing image 4638/9955
[INFO] processing image 4639/9955
[INFO] processing image 4640/9955
[INFO] processing image 4641/9955
[INFO] processing image 4642/9955
[INFO] processing image 4643/9955
[INFO] processing image 4644/9955
[INFO] processing image 4645/9955
[INFO] processing image 4646/9955
[INFO] processing image 4647/9955
[INFO] processing image 4648/9955
[INFO] processing image 4649/9955
[INFO] processing image 4650/9955
[INFO] processing image 4651/9955
[INFO] processing image 4652/9955
[INFO] processing image 4653/9955
[INFO] processing image 4654/9955
[INFO] processing image 4655/9955
[INFO] processing image 4656/9955
[INFO] processing image 4657/9955
[INFO] processing image 4658/9955
[INFO] processing image 4659/9955
[INFO] processing image 4660/9955
[INFO] processing image 4661/9955
[INFO] processing image 4662/9955
[INFO] processing image 4663/9955
[INFO] processing image 4664/9955
[INFO] processing image 4665/9955
[INFO] processing image 4666/9955
[INFO] processing image 4667/9955
[INFO] processing image 4668/9955
[INFO] processing image 4669/9955
[INFO] processing image 4670/9955
[INFO] processing image 4671/9955
[INFO] processing image 4672/9955
[INFO] processing image 4673/9955
[INFO] processing image 4674/9955
[INFO] processing image 4675/9955
[INFO] processing image 4676/9955
[INFO] processing image 4677/9955
[INFO] processing image 4678/9955
[INFO] processing image 4679/9955
[INFO] processing image 4680/9955
[INFO] processing image 4681/9955
[INFO] processing image 4682/9955
[INFO] processing image 4683/9955
[INFO] processing image 4684/9955
[INFO] processing image 4685/9955
[INFO] processing image 4686/9955
[INFO] processing image 4687/9955
[INFO] processing image 4688/9955
[INFO] processing image 4689/9955
[INFO] processing image 4690/9955
[INFO] processing image 4691/9955
[INFO] processing image 4692/9955
[INFO] processing image 4693/9955
[INFO] processing image 4694/9955
[INFO] processing image 4695/9955
[INFO] processing image 4696/9955
[INFO] processing image 4697/9955
[INFO] processing image 4698/9955
[INFO] processing image 4699/9955
[INFO] processing image 4700/9955
[INFO] processing image 4701/9955
[INFO] processing image 4702/9955
[INFO] processing image 4703/9955
[INFO] processing image 4704/9955
[INFO] processing image 4705/9955
[INFO] processing image 4706/9955
[INFO] processing image 4707/9955
[INFO] processing image 4708/9955
[INFO] processing image 4709/9955
[INFO] processing image 4710/9955
[INFO] processing image 4711/9955
[INFO] processing image 4712/9955
[INFO] processing image 4713/9955
[INFO] processing image 4714/9955
[INFO] processing image 4715/9955
[INFO] processing image 4716/9955
[INFO] processing image 4717/9955
[INFO] processing image 4718/9955
[INFO] processing image 4719/9955
[INFO] processing image 4720/9955
[INFO] processing image 4721/9955
[INFO] processing image 4722/9955
[INFO] processing image 4723/9955
[INFO] processing image 4724/9955
[INFO] processing image 4725/9955
[INFO] processing image 4726/9955
[INFO] processing image 4727/9955
[INFO] processing image 4728/9955
[INFO] processing image 4729/9955
[INFO] processing image 4730/9955
[INFO] processing image 4731/9955
[INFO] processing image 4732/9955
[INFO] processing image 4733/9955
[INFO] processing image 4734/9955
[INFO] processing image 4735/9955
[INFO] processing image 4736/9955
[INFO] processing image 4737/9955
[INFO] processing image 4738/9955
[INFO] processing image 4739/9955
[INFO] processing image 4740/9955
[INFO] processing image 4741/9955
[INFO] processing image 4742/9955
[INFO] processing image 4743/9955
[INFO] processing image 4744/9955
[INFO] processing image 4745/9955
[INFO] processing image 4746/9955
[INFO] processing image 4747/9955
[INFO] processing image 4748/9955
[INFO] processing image 4749/9955
[INFO] processing image 4750/9955
[INFO] processing image 4751/9955
[INFO] processing image 4752/9955
[INFO] processing image 4753/9955
[INFO] processing image 4754/9955
[INFO] processing image 4755/9955
[INFO] processing image 4756/9955
[INFO] processing image 4757/9955
[INFO] processing image 4758/9955
[INFO] processing image 4759/9955
[INFO] processing image 4760/9955
[INFO] processing image 4761/9955
[INFO] processing image 4762/9955
[INFO] processing image 4763/9955
[INFO] processing image 4764/9955
[INFO] processing image 4765/9955
[INFO] processing image 4766/9955
[INFO] processing image 4767/9955
[INFO] processing image 4768/9955
[INFO] processing image 4769/9955
[INFO] processing image 4770/9955
[INFO] processing image 4771/9955
[INFO] processing image 4772/9955
[INFO] processing image 4773/9955
[INFO] processing image 4774/9955
[INFO] processing image 4775/9955
[INFO] processing image 4776/9955
[INFO] processing image 4777/9955
[INFO] processing image 4778/9955
[INFO] processing image 4779/9955
[INFO] processing image 4780/9955
[INFO] processing image 4781/9955
[INFO] processing image 4782/9955
[INFO] processing image 4783/9955
[INFO] processing image 4784/9955
[INFO] processing image 4785/9955
[INFO] processing image 4786/9955
[INFO] processing image 4787/9955
[INFO] processing image 4788/9955
[INFO] processing image 4789/9955
[INFO] processing image 4790/9955
[INFO] processing image 4791/9955
[INFO] processing image 4792/9955
[INFO] processing image 4793/9955
[INFO] processing image 4794/9955
[INFO] processing image 4795/9955
[INFO] processing image 4796/9955
[INFO] processing image 4797/9955
[INFO] processing image 4798/9955
[INFO] processing image 4799/9955
[INFO] processing image 4800/9955
[INFO] processing image 4801/9955
[INFO] processing image 4802/9955
[INFO] processing image 4803/9955
[INFO] processing image 4804/9955
[INFO] processing image 4805/9955
[INFO] processing image 4806/9955
[INFO] processing image 4807/9955
[INFO] processing image 4808/9955
[INFO] processing image 4809/9955
[INFO] processing image 4810/9955
[INFO] processing image 4811/9955
[INFO] processing image 4812/9955
[INFO] processing image 4813/9955
[INFO] processing image 4814/9955
[INFO] processing image 4815/9955
[INFO] processing image 4816/9955
[INFO] processing image 4817/9955
[INFO] processing image 4818/9955
[INFO] processing image 4819/9955
[INFO] processing image 4820/9955
[INFO] processing image 4821/9955
[INFO] processing image 4822/9955
[INFO] processing image 4823/9955
[INFO] processing image 4824/9955
[INFO] processing image 4825/9955
[INFO] processing image 4826/9955
[INFO] processing image 4827/9955
[INFO] processing image 4828/9955
[INFO] processing image 4829/9955
[INFO] processing image 4830/9955
[INFO] processing image 4831/9955
[INFO] processing image 4832/9955
[INFO] processing image 4833/9955
[INFO] processing image 4834/9955
[INFO] processing image 4835/9955
[INFO] processing image 4836/9955
[INFO] processing image 4837/9955
[INFO] processing image 4838/9955
[INFO] processing image 4839/9955
[INFO] processing image 4840/9955
[INFO] processing image 4841/9955
[INFO] processing image 4842/9955
[INFO] processing image 4843/9955
[INFO] processing image 4844/9955
[INFO] processing image 4845/9955
[INFO] processing image 4846/9955
[INFO] processing image 4847/9955
[INFO] processing image 4848/9955
[INFO] processing image 4849/9955
[INFO] processing image 4850/9955
[INFO] processing image 4851/9955
[INFO] processing image 4852/9955
[INFO] processing image 4853/9955
[INFO] processing image 4854/9955
[INFO] processing image 4855/9955
[INFO] processing image 4856/9955
[INFO] processing image 4857/9955
[INFO] processing image 4858/9955
[INFO] processing image 4859/9955
[INFO] processing image 4860/9955
[INFO] processing image 4861/9955
[INFO] processing image 4862/9955
[INFO] processing image 4863/9955
[INFO] processing image 4864/9955
[INFO] processing image 4865/9955
[INFO] processing image 4866/9955
[INFO] processing image 4867/9955
[INFO] processing image 4868/9955
[INFO] processing image 4869/9955
[INFO] processing image 4870/9955
[INFO] processing image 4871/9955
[INFO] processing image 4872/9955
[INFO] processing image 4873/9955
[INFO] processing image 4874/9955
[INFO] processing image 4875/9955
[INFO] processing image 4876/9955
[INFO] processing image 4877/9955
[INFO] processing image 4878/9955
[INFO] processing image 4879/9955
[INFO] processing image 4880/9955
[INFO] processing image 4881/9955
[INFO] processing image 4882/9955
[INFO] processing image 4883/9955
[INFO] processing image 4884/9955
[INFO] processing image 4885/9955
[INFO] processing image 4886/9955
[INFO] processing image 4887/9955
[INFO] processing image 4888/9955
[INFO] processing image 4889/9955
[INFO] processing image 4890/9955
[INFO] processing image 4891/9955
[INFO] processing image 4892/9955
[INFO] processing image 4893/9955
[INFO] processing image 4894/9955
[INFO] processing image 4895/9955
[INFO] processing image 4896/9955
[INFO] processing image 4897/9955
[INFO] processing image 4898/9955
[INFO] processing image 4899/9955
[INFO] processing image 4900/9955
[INFO] processing image 4901/9955
[INFO] processing image 4902/9955
[INFO] processing image 4903/9955
[INFO] processing image 4904/9955
[INFO] processing image 4905/9955
[INFO] processing image 4906/9955
[INFO] processing image 4907/9955
[INFO] processing image 4908/9955
[INFO] processing image 4909/9955
[INFO] processing image 4910/9955
[INFO] processing image 4911/9955
[INFO] processing image 4912/9955
[INFO] processing image 4913/9955
[INFO] processing image 4914/9955
[INFO] processing image 4915/9955
[INFO] processing image 4916/9955
[INFO] processing image 4917/9955
[INFO] processing image 4918/9955
[INFO] processing image 4919/9955
[INFO] processing image 4920/9955
[INFO] processing image 4921/9955
[INFO] processing image 4922/9955
[INFO] processing image 4923/9955
[INFO] processing image 4924/9955
[INFO] processing image 4925/9955
[INFO] processing image 4926/9955
[INFO] processing image 4927/9955
[INFO] processing image 4928/9955
[INFO] processing image 4929/9955
[INFO] processing image 4930/9955
[INFO] processing image 4931/9955
[INFO] processing image 4932/9955
[INFO] processing image 4933/9955
[INFO] processing image 4934/9955
[INFO] processing image 4935/9955
[INFO] processing image 4936/9955
[INFO] processing image 4937/9955
[INFO] processing image 4938/9955
[INFO] processing image 4939/9955
[INFO] processing image 4940/9955
[INFO] processing image 4941/9955
[INFO] processing image 4942/9955
[INFO] processing image 4943/9955
[INFO] processing image 4944/9955
[INFO] processing image 4945/9955
[INFO] processing image 4946/9955
[INFO] processing image 4947/9955
[INFO] processing image 4948/9955
[INFO] processing image 4949/9955
[INFO] processing image 4950/9955
[INFO] processing image 4951/9955
[INFO] processing image 4952/9955
[INFO] processing image 4953/9955
[INFO] processing image 4954/9955
[INFO] processing image 4955/9955
[INFO] processing image 4956/9955
[INFO] processing image 4957/9955
[INFO] processing image 4958/9955
[INFO] processing image 4959/9955
[INFO] processing image 4960/9955
[INFO] processing image 4961/9955
[INFO] processing image 4962/9955
[INFO] processing image 4963/9955
[INFO] processing image 4964/9955
[INFO] processing image 4965/9955
[INFO] processing image 4966/9955
[INFO] processing image 4967/9955
[INFO] processing image 4968/9955
[INFO] processing image 4969/9955
[INFO] processing image 4970/9955
[INFO] processing image 4971/9955
[INFO] processing image 4972/9955
[INFO] processing image 4973/9955
[INFO] processing image 4974/9955
[INFO] processing image 4975/9955
[INFO] processing image 4976/9955
[INFO] processing image 4977/9955
[INFO] processing image 4978/9955
[INFO] processing image 4979/9955
[INFO] processing image 4980/9955
[INFO] processing image 4981/9955
[INFO] processing image 4982/9955
[INFO] processing image 4983/9955
[INFO] processing image 4984/9955
[INFO] processing image 4985/9955
[INFO] processing image 4986/9955
[INFO] processing image 4987/9955
[INFO] processing image 4988/9955
[INFO] processing image 4989/9955
[INFO] processing image 4990/9955
[INFO] processing image 4991/9955
[INFO] processing image 4992/9955
[INFO] processing image 4993/9955
[INFO] processing image 4994/9955
[INFO] processing image 4995/9955
[INFO] processing image 4996/9955
[INFO] processing image 4997/9955
[INFO] processing image 4998/9955
[INFO] processing image 4999/9955
[INFO] processing image 5000/9955
[INFO] processing image 5001/9955
[INFO] processing image 5002/9955
[INFO] processing image 5003/9955
[INFO] processing image 5004/9955
[INFO] processing image 5005/9955
[INFO] processing image 5006/9955
[INFO] processing image 5007/9955
[INFO] processing image 5008/9955
[INFO] processing image 5009/9955
[INFO] processing image 5010/9955
[INFO] processing image 5011/9955
[INFO] processing image 5012/9955
[INFO] processing image 5013/9955
[INFO] processing image 5014/9955
[INFO] processing image 5015/9955
[INFO] processing image 5016/9955
[INFO] processing image 5017/9955
[INFO] processing image 5018/9955
[INFO] processing image 5019/9955
[INFO] processing image 5020/9955
[INFO] processing image 5021/9955
[INFO] processing image 5022/9955
[INFO] processing image 5023/9955
[INFO] processing image 5024/9955
[INFO] processing image 5025/9955
[INFO] processing image 5026/9955
[INFO] processing image 5027/9955
[INFO] processing image 5028/9955
[INFO] processing image 5029/9955
[INFO] processing image 5030/9955
[INFO] processing image 5031/9955
[INFO] processing image 5032/9955
[INFO] processing image 5033/9955
[INFO] processing image 5034/9955
[INFO] processing image 5035/9955
[INFO] processing image 5036/9955
[INFO] processing image 5037/9955
[INFO] processing image 5038/9955
[INFO] processing image 5039/9955
[INFO] processing image 5040/9955
[INFO] processing image 5041/9955
[INFO] processing image 5042/9955
[INFO] processing image 5043/9955
[INFO] processing image 5044/9955
[INFO] processing image 5045/9955
[INFO] processing image 5046/9955
[INFO] processing image 5047/9955
[INFO] processing image 5048/9955
[INFO] processing image 5049/9955
[INFO] processing image 5050/9955
[INFO] processing image 5051/9955
[INFO] processing image 5052/9955
[INFO] processing image 5053/9955
[INFO] processing image 5054/9955
[INFO] processing image 5055/9955
[INFO] processing image 5056/9955
[INFO] processing image 5057/9955
[INFO] processing image 5058/9955
[INFO] processing image 5059/9955
[INFO] processing image 5060/9955
[INFO] processing image 5061/9955
[INFO] processing image 5062/9955
[INFO] processing image 5063/9955
[INFO] processing image 5064/9955
[INFO] processing image 5065/9955
[INFO] processing image 5066/9955
[INFO] processing image 5067/9955
[INFO] processing image 5068/9955
[INFO] processing image 5069/9955
[INFO] processing image 5070/9955
[INFO] processing image 5071/9955
[INFO] processing image 5072/9955
[INFO] processing image 5073/9955
[INFO] processing image 5074/9955
[INFO] processing image 5075/9955
[INFO] processing image 5076/9955
[INFO] processing image 5077/9955
[INFO] processing image 5078/9955
[INFO] processing image 5079/9955
[INFO] processing image 5080/9955
[INFO] processing image 5081/9955
[INFO] processing image 5082/9955
[INFO] processing image 5083/9955
[INFO] processing image 5084/9955
[INFO] processing image 5085/9955
[INFO] processing image 5086/9955
[INFO] processing image 5087/9955
[INFO] processing image 5088/9955
[INFO] processing image 5089/9955
[INFO] processing image 5090/9955
[INFO] processing image 5091/9955
[INFO] processing image 5092/9955
[INFO] processing image 5093/9955
[INFO] processing image 5094/9955
[INFO] processing image 5095/9955
[INFO] processing image 5096/9955
[INFO] processing image 5097/9955
[INFO] processing image 5098/9955
[INFO] processing image 5099/9955
[INFO] processing image 5100/9955
[INFO] processing image 5101/9955
[INFO] processing image 5102/9955
[INFO] processing image 5103/9955
[INFO] processing image 5104/9955
[INFO] processing image 5105/9955
[INFO] processing image 5106/9955
[INFO] processing image 5107/9955
[INFO] processing image 5108/9955
[INFO] processing image 5109/9955
[INFO] processing image 5110/9955
[INFO] processing image 5111/9955
[INFO] processing image 5112/9955
[INFO] processing image 5113/9955
[INFO] processing image 5114/9955
[INFO] processing image 5115/9955
[INFO] processing image 5116/9955
[INFO] processing image 5117/9955
[INFO] processing image 5118/9955
[INFO] processing image 5119/9955
[INFO] processing image 5120/9955
[INFO] processing image 5121/9955
[INFO] processing image 5122/9955
[INFO] processing image 5123/9955
[INFO] processing image 5124/9955
[INFO] processing image 5125/9955
[INFO] processing image 5126/9955
[INFO] processing image 5127/9955
[INFO] processing image 5128/9955
[INFO] processing image 5129/9955
[INFO] processing image 5130/9955
[INFO] processing image 5131/9955
[INFO] processing image 5132/9955
[INFO] processing image 5133/9955
[INFO] processing image 5134/9955
[INFO] processing image 5135/9955
[INFO] processing image 5136/9955
[INFO] processing image 5137/9955
[INFO] processing image 5138/9955
[INFO] processing image 5139/9955
[INFO] processing image 5140/9955
[INFO] processing image 5141/9955
[INFO] processing image 5142/9955
[INFO] processing image 5143/9955
[INFO] processing image 5144/9955
[INFO] processing image 5145/9955
[INFO] processing image 5146/9955
[INFO] processing image 5147/9955
[INFO] processing image 5148/9955
[INFO] processing image 5149/9955
[INFO] processing image 5150/9955
[INFO] processing image 5151/9955
[INFO] processing image 5152/9955
[INFO] processing image 5153/9955
[INFO] processing image 5154/9955
[INFO] processing image 5155/9955
[INFO] processing image 5156/9955
[INFO] processing image 5157/9955
[INFO] processing image 5158/9955
[INFO] processing image 5159/9955
[INFO] processing image 5160/9955
[INFO] processing image 5161/9955
[INFO] processing image 5162/9955
[INFO] processing image 5163/9955
[INFO] processing image 5164/9955
[INFO] processing image 5165/9955
[INFO] processing image 5166/9955
[INFO] processing image 5167/9955
[INFO] processing image 5168/9955
[INFO] processing image 5169/9955
[INFO] processing image 5170/9955
[INFO] processing image 5171/9955
[INFO] processing image 5172/9955
[INFO] processing image 5173/9955
[INFO] processing image 5174/9955
[INFO] processing image 5175/9955
[INFO] processing image 5176/9955
[INFO] processing image 5177/9955
[INFO] processing image 5178/9955
[INFO] processing image 5179/9955
[INFO] processing image 5180/9955
[INFO] processing image 5181/9955
[INFO] processing image 5182/9955
[INFO] processing image 5183/9955
[INFO] processing image 5184/9955
[INFO] processing image 5185/9955
[INFO] processing image 5186/9955
[INFO] processing image 5187/9955
[INFO] processing image 5188/9955
[INFO] processing image 5189/9955
[INFO] processing image 5190/9955
[INFO] processing image 5191/9955
[INFO] processing image 5192/9955
[INFO] processing image 5193/9955
[INFO] processing image 5194/9955
[INFO] processing image 5195/9955
[INFO] processing image 5196/9955
[INFO] processing image 5197/9955
[INFO] processing image 5198/9955
[INFO] processing image 5199/9955
[INFO] processing image 5200/9955
[INFO] processing image 5201/9955
[INFO] processing image 5202/9955
[INFO] processing image 5203/9955
[INFO] processing image 5204/9955
[INFO] processing image 5205/9955
[INFO] processing image 5206/9955
[INFO] processing image 5207/9955
[INFO] processing image 5208/9955
[INFO] processing image 5209/9955
[INFO] processing image 5210/9955
[INFO] processing image 5211/9955
[INFO] processing image 5212/9955
[INFO] processing image 5213/9955
[INFO] processing image 5214/9955
[INFO] processing image 5215/9955
[INFO] processing image 5216/9955
[INFO] processing image 5217/9955
[INFO] processing image 5218/9955
[INFO] processing image 5219/9955
[INFO] processing image 5220/9955
[INFO] processing image 5221/9955
[INFO] processing image 5222/9955
[INFO] processing image 5223/9955
[INFO] processing image 5224/9955
[INFO] processing image 5225/9955
[INFO] processing image 5226/9955
[INFO] processing image 5227/9955
[INFO] processing image 5228/9955
[INFO] processing image 5229/9955
[INFO] processing image 5230/9955
[INFO] processing image 5231/9955
[INFO] processing image 5232/9955
[INFO] processing image 5233/9955
[INFO] processing image 5234/9955
[INFO] processing image 5235/9955
[INFO] processing image 5236/9955
[INFO] processing image 5237/9955
[INFO] processing image 5238/9955
[INFO] processing image 5239/9955
[INFO] processing image 5240/9955
[INFO] processing image 5241/9955
[INFO] processing image 5242/9955
[INFO] processing image 5243/9955
[INFO] processing image 5244/9955
[INFO] processing image 5245/9955
[INFO] processing image 5246/9955
[INFO] processing image 5247/9955
[INFO] processing image 5248/9955
[INFO] processing image 5249/9955
[INFO] processing image 5250/9955
[INFO] processing image 5251/9955
[INFO] processing image 5252/9955
[INFO] processing image 5253/9955
[INFO] processing image 5254/9955
[INFO] processing image 5255/9955
[INFO] processing image 5256/9955
[INFO] processing image 5257/9955
[INFO] processing image 5258/9955
[INFO] processing image 5259/9955
[INFO] processing image 5260/9955
[INFO] processing image 5261/9955
[INFO] processing image 5262/9955
[INFO] processing image 5263/9955
[INFO] processing image 5264/9955
[INFO] processing image 5265/9955
[INFO] processing image 5266/9955
[INFO] processing image 5267/9955
[INFO] processing image 5268/9955
[INFO] processing image 5269/9955
[INFO] processing image 5270/9955
[INFO] processing image 5271/9955
[INFO] processing image 5272/9955
[INFO] processing image 5273/9955
[INFO] processing image 5274/9955
[INFO] processing image 5275/9955
[INFO] processing image 5276/9955
[INFO] processing image 5277/9955
[INFO] processing image 5278/9955
[INFO] processing image 5279/9955
[INFO] processing image 5280/9955
[INFO] processing image 5281/9955
[INFO] processing image 5282/9955
[INFO] processing image 5283/9955
[INFO] processing image 5284/9955
[INFO] processing image 5285/9955
[INFO] processing image 5286/9955
[INFO] processing image 5287/9955
[INFO] processing image 5288/9955
[INFO] processing image 5289/9955
[INFO] processing image 5290/9955
[INFO] processing image 5291/9955
[INFO] processing image 5292/9955
[INFO] processing image 5293/9955
[INFO] processing image 5294/9955
[INFO] processing image 5295/9955
[INFO] processing image 5296/9955
[INFO] processing image 5297/9955
[INFO] processing image 5298/9955
[INFO] processing image 5299/9955
[INFO] processing image 5300/9955
[INFO] processing image 5301/9955
[INFO] processing image 5302/9955
[INFO] processing image 5303/9955
[INFO] processing image 5304/9955
[INFO] processing image 5305/9955
[INFO] processing image 5306/9955
[INFO] processing image 5307/9955
[INFO] processing image 5308/9955
[INFO] processing image 5309/9955
[INFO] processing image 5310/9955
[INFO] processing image 5311/9955
[INFO] processing image 5312/9955
[INFO] processing image 5313/9955
[INFO] processing image 5314/9955
[INFO] processing image 5315/9955
[INFO] processing image 5316/9955
[INFO] processing image 5317/9955
[INFO] processing image 5318/9955
[INFO] processing image 5319/9955
[INFO] processing image 5320/9955
[INFO] processing image 5321/9955
[INFO] processing image 5322/9955
[INFO] processing image 5323/9955
[INFO] processing image 5324/9955
[INFO] processing image 5325/9955
[INFO] processing image 5326/9955
[INFO] processing image 5327/9955
[INFO] processing image 5328/9955
[INFO] processing image 5329/9955
[INFO] processing image 5330/9955
[INFO] processing image 5331/9955
[INFO] processing image 5332/9955
[INFO] processing image 5333/9955
[INFO] processing image 5334/9955
[INFO] processing image 5335/9955
[INFO] processing image 5336/9955
[INFO] processing image 5337/9955
[INFO] processing image 5338/9955
[INFO] processing image 5339/9955
[INFO] processing image 5340/9955
[INFO] processing image 5341/9955
[INFO] processing image 5342/9955
[INFO] processing image 5343/9955
[INFO] processing image 5344/9955
[INFO] processing image 5345/9955
[INFO] processing image 5346/9955
[INFO] processing image 5347/9955
[INFO] processing image 5348/9955
[INFO] processing image 5349/9955
[INFO] processing image 5350/9955
[INFO] processing image 5351/9955
[INFO] processing image 5352/9955
[INFO] processing image 5353/9955
[INFO] processing image 5354/9955
[INFO] processing image 5355/9955
[INFO] processing image 5356/9955
[INFO] processing image 5357/9955
[INFO] processing image 5358/9955
[INFO] processing image 5359/9955
[INFO] processing image 5360/9955
[INFO] processing image 5361/9955
[INFO] processing image 5362/9955
[INFO] processing image 5363/9955
[INFO] processing image 5364/9955
[INFO] processing image 5365/9955
[INFO] processing image 5366/9955
[INFO] processing image 5367/9955
[INFO] processing image 5368/9955
[INFO] processing image 5369/9955
[INFO] processing image 5370/9955
[INFO] processing image 5371/9955
[INFO] processing image 5372/9955
[INFO] processing image 5373/9955
[INFO] processing image 5374/9955
[INFO] processing image 5375/9955
[INFO] processing image 5376/9955
[INFO] processing image 5377/9955
[INFO] processing image 5378/9955
[INFO] processing image 5379/9955
[INFO] processing image 5380/9955
[INFO] processing image 5381/9955
[INFO] processing image 5382/9955
[INFO] processing image 5383/9955
[INFO] processing image 5384/9955
[INFO] processing image 5385/9955
[INFO] processing image 5386/9955
[INFO] processing image 5387/9955
[INFO] processing image 5388/9955
[INFO] processing image 5389/9955
[INFO] processing image 5390/9955
[INFO] processing image 5391/9955
[INFO] processing image 5392/9955
[INFO] processing image 5393/9955
[INFO] processing image 5394/9955
[INFO] processing image 5395/9955
[INFO] processing image 5396/9955
[INFO] processing image 5397/9955
[INFO] processing image 5398/9955
[INFO] processing image 5399/9955
[INFO] processing image 5400/9955
[INFO] processing image 5401/9955
[INFO] processing image 5402/9955
[INFO] processing image 5403/9955
[INFO] processing image 5404/9955
[INFO] processing image 5405/9955
[INFO] processing image 5406/9955
[INFO] processing image 5407/9955
[INFO] processing image 5408/9955
[INFO] processing image 5409/9955
[INFO] processing image 5410/9955
[INFO] processing image 5411/9955
[INFO] processing image 5412/9955
[INFO] processing image 5413/9955
[INFO] processing image 5414/9955
[INFO] processing image 5415/9955
[INFO] processing image 5416/9955
[INFO] processing image 5417/9955
[INFO] processing image 5418/9955
[INFO] processing image 5419/9955
[INFO] processing image 5420/9955
[INFO] processing image 5421/9955
[INFO] processing image 5422/9955
[INFO] processing image 5423/9955
[INFO] processing image 5424/9955
[INFO] processing image 5425/9955
[INFO] processing image 5426/9955
[INFO] processing image 5427/9955
[INFO] processing image 5428/9955
[INFO] processing image 5429/9955
[INFO] processing image 5430/9955
[INFO] processing image 5431/9955
[INFO] processing image 5432/9955
[INFO] processing image 5433/9955
[INFO] processing image 5434/9955
[INFO] processing image 5435/9955
[INFO] processing image 5436/9955
[INFO] processing image 5437/9955
[INFO] processing image 5438/9955
[INFO] processing image 5439/9955
[INFO] processing image 5440/9955
[INFO] processing image 5441/9955
[INFO] processing image 5442/9955
[INFO] processing image 5443/9955
[INFO] processing image 5444/9955
[INFO] processing image 5445/9955
[INFO] processing image 5446/9955
[INFO] processing image 5447/9955
[INFO] processing image 5448/9955
[INFO] processing image 5449/9955
[INFO] processing image 5450/9955
[INFO] processing image 5451/9955
[INFO] processing image 5452/9955
[INFO] processing image 5453/9955
[INFO] processing image 5454/9955
[INFO] processing image 5455/9955
[INFO] processing image 5456/9955
[INFO] processing image 5457/9955
[INFO] processing image 5458/9955
[INFO] processing image 5459/9955
[INFO] processing image 5460/9955
[INFO] processing image 5461/9955
[INFO] processing image 5462/9955
[INFO] processing image 5463/9955
[INFO] processing image 5464/9955
[INFO] processing image 5465/9955
[INFO] processing image 5466/9955
[INFO] processing image 5467/9955
[INFO] processing image 5468/9955
[INFO] processing image 5469/9955
[INFO] processing image 5470/9955
[INFO] processing image 5471/9955
[INFO] processing image 5472/9955
[INFO] processing image 5473/9955
[INFO] processing image 5474/9955
[INFO] processing image 5475/9955
[INFO] processing image 5476/9955
[INFO] processing image 5477/9955
[INFO] processing image 5478/9955
[INFO] processing image 5479/9955
[INFO] processing image 5480/9955
[INFO] processing image 5481/9955
[INFO] processing image 5482/9955
[INFO] processing image 5483/9955
[INFO] processing image 5484/9955
[INFO] processing image 5485/9955
[INFO] processing image 5486/9955
[INFO] processing image 5487/9955
[INFO] processing image 5488/9955
[INFO] processing image 5489/9955
[INFO] processing image 5490/9955
[INFO] processing image 5491/9955
[INFO] processing image 5492/9955
[INFO] processing image 5493/9955
[INFO] processing image 5494/9955
[INFO] processing image 5495/9955
[INFO] processing image 5496/9955
[INFO] processing image 5497/9955
[INFO] processing image 5498/9955
[INFO] processing image 5499/9955
[INFO] processing image 5500/9955
[INFO] processing image 5501/9955
[INFO] processing image 5502/9955
[INFO] processing image 5503/9955
[INFO] processing image 5504/9955
[INFO] processing image 5505/9955
[INFO] processing image 5506/9955
[INFO] processing image 5507/9955
[INFO] processing image 5508/9955
[INFO] processing image 5509/9955
[INFO] processing image 5510/9955
[INFO] processing image 5511/9955
[INFO] processing image 5512/9955
[INFO] processing image 5513/9955
[INFO] processing image 5514/9955
[INFO] processing image 5515/9955
[INFO] processing image 5516/9955
[INFO] processing image 5517/9955
[INFO] processing image 5518/9955
[INFO] processing image 5519/9955
[INFO] processing image 5520/9955
[INFO] processing image 5521/9955
[INFO] processing image 5522/9955
[INFO] processing image 5523/9955
[INFO] processing image 5524/9955
[INFO] processing image 5525/9955
[INFO] processing image 5526/9955
[INFO] processing image 5527/9955
[INFO] processing image 5528/9955
[INFO] processing image 5529/9955
[INFO] processing image 5530/9955
[INFO] processing image 5531/9955
[INFO] processing image 5532/9955
[INFO] processing image 5533/9955
[INFO] processing image 5534/9955
[INFO] processing image 5535/9955
[INFO] processing image 5536/9955
[INFO] processing image 5537/9955
[INFO] processing image 5538/9955
[INFO] processing image 5539/9955
[INFO] processing image 5540/9955
[INFO] processing image 5541/9955
[INFO] processing image 5542/9955
[INFO] processing image 5543/9955
[INFO] processing image 5544/9955
[INFO] processing image 5545/9955
[INFO] processing image 5546/9955
[INFO] processing image 5547/9955
[INFO] processing image 5548/9955
[INFO] processing image 5549/9955
[INFO] processing image 5550/9955
[INFO] processing image 5551/9955
[INFO] processing image 5552/9955
[INFO] processing image 5553/9955
[INFO] processing image 5554/9955
[INFO] processing image 5555/9955
[INFO] processing image 5556/9955
[INFO] processing image 5557/9955
[INFO] processing image 5558/9955
[INFO] processing image 5559/9955
[INFO] processing image 5560/9955
[INFO] processing image 5561/9955
[INFO] processing image 5562/9955
[INFO] processing image 5563/9955
[INFO] processing image 5564/9955
[INFO] processing image 5565/9955
[INFO] processing image 5566/9955
[INFO] processing image 5567/9955
[INFO] processing image 5568/9955
[INFO] processing image 5569/9955
[INFO] processing image 5570/9955
[INFO] processing image 5571/9955
[INFO] processing image 5572/9955
[INFO] processing image 5573/9955
[INFO] processing image 5574/9955
[INFO] processing image 5575/9955
[INFO] processing image 5576/9955
[INFO] processing image 5577/9955
[INFO] processing image 5578/9955
[INFO] processing image 5579/9955
[INFO] processing image 5580/9955
[INFO] processing image 5581/9955
[INFO] processing image 5582/9955
[INFO] processing image 5583/9955
[INFO] processing image 5584/9955
[INFO] processing image 5585/9955
[INFO] processing image 5586/9955
[INFO] processing image 5587/9955
[INFO] processing image 5588/9955
[INFO] processing image 5589/9955
[INFO] processing image 5590/9955
[INFO] processing image 5591/9955
[INFO] processing image 5592/9955
[INFO] processing image 5593/9955
[INFO] processing image 5594/9955
[INFO] processing image 5595/9955
[INFO] processing image 5596/9955
[INFO] processing image 5597/9955
[INFO] processing image 5598/9955
[INFO] processing image 5599/9955
[INFO] processing image 5600/9955
[INFO] processing image 5601/9955
[INFO] processing image 5602/9955
[INFO] processing image 5603/9955
[INFO] processing image 5604/9955
[INFO] processing image 5605/9955
[INFO] processing image 5606/9955
[INFO] processing image 5607/9955
[INFO] processing image 5608/9955
[INFO] processing image 5609/9955
[INFO] processing image 5610/9955
[INFO] processing image 5611/9955
[INFO] processing image 5612/9955
[INFO] processing image 5613/9955
[INFO] processing image 5614/9955
[INFO] processing image 5615/9955
[INFO] processing image 5616/9955
[INFO] processing image 5617/9955
[INFO] processing image 5618/9955
[INFO] processing image 5619/9955
[INFO] processing image 5620/9955
[INFO] processing image 5621/9955
[INFO] processing image 5622/9955
[INFO] processing image 5623/9955
[INFO] processing image 5624/9955
[INFO] processing image 5625/9955
[INFO] processing image 5626/9955
[INFO] processing image 5627/9955
[INFO] processing image 5628/9955
[INFO] processing image 5629/9955
[INFO] processing image 5630/9955
[INFO] processing image 5631/9955
[INFO] processing image 5632/9955
[INFO] processing image 5633/9955
[INFO] processing image 5634/9955
[INFO] processing image 5635/9955
[INFO] processing image 5636/9955
[INFO] processing image 5637/9955
[INFO] processing image 5638/9955
[INFO] processing image 5639/9955
[INFO] processing image 5640/9955
[INFO] processing image 5641/9955
[INFO] processing image 5642/9955
[INFO] processing image 5643/9955
[INFO] processing image 5644/9955
[INFO] processing image 5645/9955
[INFO] processing image 5646/9955
[INFO] processing image 5647/9955
[INFO] processing image 5648/9955
[INFO] processing image 5649/9955
[INFO] processing image 5650/9955
[INFO] processing image 5651/9955
[INFO] processing image 5652/9955
[INFO] processing image 5653/9955
[INFO] processing image 5654/9955
[INFO] processing image 5655/9955
[INFO] processing image 5656/9955
[INFO] processing image 5657/9955
[INFO] processing image 5658/9955
[INFO] processing image 5659/9955
[INFO] processing image 5660/9955
[INFO] processing image 5661/9955
[INFO] processing image 5662/9955
[INFO] processing image 5663/9955
[INFO] processing image 5664/9955
[INFO] processing image 5665/9955
[INFO] processing image 5666/9955
[INFO] processing image 5667/9955
[INFO] processing image 5668/9955
[INFO] processing image 5669/9955
[INFO] processing image 5670/9955
[INFO] processing image 5671/9955
[INFO] processing image 5672/9955
[INFO] processing image 5673/9955
[INFO] processing image 5674/9955
[INFO] processing image 5675/9955
[INFO] processing image 5676/9955
[INFO] processing image 5677/9955
[INFO] processing image 5678/9955
[INFO] processing image 5679/9955
[INFO] processing image 5680/9955
[INFO] processing image 5681/9955
[INFO] processing image 5682/9955
[INFO] processing image 5683/9955
[INFO] processing image 5684/9955
[INFO] processing image 5685/9955
[INFO] processing image 5686/9955
[INFO] processing image 5687/9955
[INFO] processing image 5688/9955
[INFO] processing image 5689/9955
[INFO] processing image 5690/9955
[INFO] processing image 5691/9955
[INFO] processing image 5692/9955
[INFO] processing image 5693/9955
[INFO] processing image 5694/9955
[INFO] processing image 5695/9955
[INFO] processing image 5696/9955
[INFO] processing image 5697/9955
[INFO] processing image 5698/9955
[INFO] processing image 5699/9955
[INFO] processing image 5700/9955
[INFO] processing image 5701/9955
[INFO] processing image 5702/9955
[INFO] processing image 5703/9955
[INFO] processing image 5704/9955
[INFO] processing image 5705/9955
[INFO] processing image 5706/9955
[INFO] processing image 5707/9955
[INFO] processing image 5708/9955
[INFO] processing image 5709/9955
[INFO] processing image 5710/9955
[INFO] processing image 5711/9955
[INFO] processing image 5712/9955
[INFO] processing image 5713/9955
[INFO] processing image 5714/9955
[INFO] processing image 5715/9955
[INFO] processing image 5716/9955
[INFO] processing image 5717/9955
[INFO] processing image 5718/9955
[INFO] processing image 5719/9955
[INFO] processing image 5720/9955
[INFO] processing image 5721/9955
[INFO] processing image 5722/9955
[INFO] processing image 5723/9955
[INFO] processing image 5724/9955
[INFO] processing image 5725/9955
[INFO] processing image 5726/9955
[INFO] processing image 5727/9955
[INFO] processing image 5728/9955
[INFO] processing image 5729/9955
[INFO] processing image 5730/9955
[INFO] processing image 5731/9955
[INFO] processing image 5732/9955
[INFO] processing image 5733/9955
[INFO] processing image 5734/9955
[INFO] processing image 5735/9955
[INFO] processing image 5736/9955
[INFO] processing image 5737/9955
[INFO] processing image 5738/9955
[INFO] processing image 5739/9955
[INFO] processing image 5740/9955
[INFO] processing image 5741/9955
[INFO] processing image 5742/9955
[INFO] processing image 5743/9955
[INFO] processing image 5744/9955
[INFO] processing image 5745/9955
[INFO] processing image 5746/9955
[INFO] processing image 5747/9955
[INFO] processing image 5748/9955
[INFO] processing image 5749/9955
[INFO] processing image 5750/9955
[INFO] processing image 5751/9955
[INFO] processing image 5752/9955
[INFO] processing image 5753/9955
[INFO] processing image 5754/9955
[INFO] processing image 5755/9955
[INFO] processing image 5756/9955
[INFO] processing image 5757/9955
[INFO] processing image 5758/9955
[INFO] processing image 5759/9955
[INFO] processing image 5760/9955
[INFO] processing image 5761/9955
[INFO] processing image 5762/9955
[INFO] processing image 5763/9955
[INFO] processing image 5764/9955
[INFO] processing image 5765/9955
[INFO] processing image 5766/9955
[INFO] processing image 5767/9955
[INFO] processing image 5768/9955
[INFO] processing image 5769/9955
[INFO] processing image 5770/9955
[INFO] processing image 5771/9955
[INFO] processing image 5772/9955
[INFO] processing image 5773/9955
[INFO] processing image 5774/9955
[INFO] processing image 5775/9955
[INFO] processing image 5776/9955
[INFO] processing image 5777/9955
[INFO] processing image 5778/9955
[INFO] processing image 5779/9955
[INFO] processing image 5780/9955
[INFO] processing image 5781/9955
[INFO] processing image 5782/9955
[INFO] processing image 5783/9955
[INFO] processing image 5784/9955
[INFO] processing image 5785/9955
[INFO] processing image 5786/9955
[INFO] processing image 5787/9955
[INFO] processing image 5788/9955
[INFO] processing image 5789/9955
[INFO] processing image 5790/9955
[INFO] processing image 5791/9955
[INFO] processing image 5792/9955
[INFO] processing image 5793/9955
[INFO] processing image 5794/9955
[INFO] processing image 5795/9955
[INFO] processing image 5796/9955
[INFO] processing image 5797/9955
[INFO] processing image 5798/9955
[INFO] processing image 5799/9955
[INFO] processing image 5800/9955
[INFO] processing image 5801/9955
[INFO] processing image 5802/9955
[INFO] processing image 5803/9955
[INFO] processing image 5804/9955
[INFO] processing image 5805/9955
[INFO] processing image 5806/9955
[INFO] processing image 5807/9955
[INFO] processing image 5808/9955
[INFO] processing image 5809/9955
[INFO] processing image 5810/9955
[INFO] processing image 5811/9955
[INFO] processing image 5812/9955
[INFO] processing image 5813/9955
[INFO] processing image 5814/9955
[INFO] processing image 5815/9955
[INFO] processing image 5816/9955
[INFO] processing image 5817/9955
[INFO] processing image 5818/9955
[INFO] processing image 5819/9955
[INFO] processing image 5820/9955
[INFO] processing image 5821/9955
[INFO] processing image 5822/9955
[INFO] processing image 5823/9955
[INFO] processing image 5824/9955
[INFO] processing image 5825/9955
[INFO] processing image 5826/9955
[INFO] processing image 5827/9955
[INFO] processing image 5828/9955
[INFO] processing image 5829/9955
[INFO] processing image 5830/9955
[INFO] processing image 5831/9955
[INFO] processing image 5832/9955
[INFO] processing image 5833/9955
[INFO] processing image 5834/9955
[INFO] processing image 5835/9955
[INFO] processing image 5836/9955
[INFO] processing image 5837/9955
[INFO] processing image 5838/9955
[INFO] processing image 5839/9955
[INFO] processing image 5840/9955
[INFO] processing image 5841/9955
[INFO] processing image 5842/9955
[INFO] processing image 5843/9955
[INFO] processing image 5844/9955
[INFO] processing image 5845/9955
[INFO] processing image 5846/9955
[INFO] processing image 5847/9955
[INFO] processing image 5848/9955
[INFO] processing image 5849/9955
[INFO] processing image 5850/9955
[INFO] processing image 5851/9955
[INFO] processing image 5852/9955
[INFO] processing image 5853/9955
[INFO] processing image 5854/9955
[INFO] processing image 5855/9955
[INFO] processing image 5856/9955
[INFO] processing image 5857/9955
[INFO] processing image 5858/9955
[INFO] processing image 5859/9955
[INFO] processing image 5860/9955
[INFO] processing image 5861/9955
[INFO] processing image 5862/9955
[INFO] processing image 5863/9955
[INFO] processing image 5864/9955
[INFO] processing image 5865/9955
[INFO] processing image 5866/9955
[INFO] processing image 5867/9955
[INFO] processing image 5868/9955
[INFO] processing image 5869/9955
[INFO] processing image 5870/9955
[INFO] processing image 5871/9955
[INFO] processing image 5872/9955
[INFO] processing image 5873/9955
[INFO] processing image 5874/9955
[INFO] processing image 5875/9955
[INFO] processing image 5876/9955
[INFO] processing image 5877/9955
[INFO] processing image 5878/9955
[INFO] processing image 5879/9955
[INFO] processing image 5880/9955
[INFO] processing image 5881/9955
[INFO] processing image 5882/9955
[INFO] processing image 5883/9955
[INFO] processing image 5884/9955
[INFO] processing image 5885/9955
[INFO] processing image 5886/9955
[INFO] processing image 5887/9955
[INFO] processing image 5888/9955
[INFO] processing image 5889/9955
[INFO] processing image 5890/9955
[INFO] processing image 5891/9955
[INFO] processing image 5892/9955
[INFO] processing image 5893/9955
[INFO] processing image 5894/9955
[INFO] processing image 5895/9955
[INFO] processing image 5896/9955
[INFO] processing image 5897/9955
[INFO] processing image 5898/9955
[INFO] processing image 5899/9955
[INFO] processing image 5900/9955
[INFO] processing image 5901/9955
[INFO] processing image 5902/9955
[INFO] processing image 5903/9955
[INFO] processing image 5904/9955
[INFO] processing image 5905/9955
[INFO] processing image 5906/9955
[INFO] processing image 5907/9955
[INFO] processing image 5908/9955
[INFO] processing image 5909/9955
[INFO] processing image 5910/9955
[INFO] processing image 5911/9955
[INFO] processing image 5912/9955
[INFO] processing image 5913/9955
[INFO] processing image 5914/9955
[INFO] processing image 5915/9955
[INFO] processing image 5916/9955
[INFO] processing image 5917/9955
[INFO] processing image 5918/9955
[INFO] processing image 5919/9955
[INFO] processing image 5920/9955
[INFO] processing image 5921/9955
[INFO] processing image 5922/9955
[INFO] processing image 5923/9955
[INFO] processing image 5924/9955
[INFO] processing image 5925/9955
[INFO] processing image 5926/9955
[INFO] processing image 5927/9955
[INFO] processing image 5928/9955
[INFO] processing image 5929/9955
[INFO] processing image 5930/9955
[INFO] processing image 5931/9955
[INFO] processing image 5932/9955
[INFO] processing image 5933/9955
[INFO] processing image 5934/9955
[INFO] processing image 5935/9955
[INFO] processing image 5936/9955
[INFO] processing image 5937/9955
[INFO] processing image 5938/9955
[INFO] processing image 5939/9955
[INFO] processing image 5940/9955
[INFO] processing image 5941/9955
[INFO] processing image 5942/9955
[INFO] processing image 5943/9955
[INFO] processing image 5944/9955
[INFO] processing image 5945/9955
[INFO] processing image 5946/9955
[INFO] processing image 5947/9955
[INFO] processing image 5948/9955
[INFO] processing image 5949/9955
[INFO] processing image 5950/9955
[INFO] processing image 5951/9955
[INFO] processing image 5952/9955
[INFO] processing image 5953/9955
[INFO] processing image 5954/9955
[INFO] processing image 5955/9955
[INFO] processing image 5956/9955
[INFO] processing image 5957/9955
[INFO] processing image 5958/9955
[INFO] processing image 5959/9955
[INFO] processing image 5960/9955
[INFO] processing image 5961/9955
[INFO] processing image 5962/9955
[INFO] processing image 5963/9955
[INFO] processing image 5964/9955
[INFO] processing image 5965/9955
[INFO] processing image 5966/9955
[INFO] processing image 5967/9955
[INFO] processing image 5968/9955
[INFO] processing image 5969/9955
[INFO] processing image 5970/9955
[INFO] processing image 5971/9955
[INFO] processing image 5972/9955
[INFO] processing image 5973/9955
[INFO] processing image 5974/9955
[INFO] processing image 5975/9955
[INFO] processing image 5976/9955
[INFO] processing image 5977/9955
[INFO] processing image 5978/9955
[INFO] processing image 5979/9955
[INFO] processing image 5980/9955
[INFO] processing image 5981/9955
[INFO] processing image 5982/9955
[INFO] processing image 5983/9955
[INFO] processing image 5984/9955
[INFO] processing image 5985/9955
[INFO] processing image 5986/9955
[INFO] processing image 5987/9955
[INFO] processing image 5988/9955
[INFO] processing image 5989/9955
[INFO] processing image 5990/9955
[INFO] processing image 5991/9955
[INFO] processing image 5992/9955
[INFO] processing image 5993/9955
[INFO] processing image 5994/9955
[INFO] processing image 5995/9955
[INFO] processing image 5996/9955
[INFO] processing image 5997/9955
[INFO] processing image 5998/9955
[INFO] processing image 5999/9955
[INFO] processing image 6000/9955
[INFO] processing image 6001/9955
[INFO] processing image 6002/9955
[INFO] processing image 6003/9955
[INFO] processing image 6004/9955
[INFO] processing image 6005/9955
[INFO] processing image 6006/9955
[INFO] processing image 6007/9955
[INFO] processing image 6008/9955
[INFO] processing image 6009/9955
[INFO] processing image 6010/9955
[INFO] processing image 6011/9955
[INFO] processing image 6012/9955
[INFO] processing image 6013/9955
[INFO] processing image 6014/9955
[INFO] processing image 6015/9955
[INFO] processing image 6016/9955
[INFO] processing image 6017/9955
[INFO] processing image 6018/9955
[INFO] processing image 6019/9955
[INFO] processing image 6020/9955
[INFO] processing image 6021/9955
[INFO] processing image 6022/9955
[INFO] processing image 6023/9955
[INFO] processing image 6024/9955
[INFO] processing image 6025/9955
[INFO] processing image 6026/9955
[INFO] processing image 6027/9955
[INFO] processing image 6028/9955
[INFO] processing image 6029/9955
[INFO] processing image 6030/9955
[INFO] processing image 6031/9955
[INFO] processing image 6032/9955
[INFO] processing image 6033/9955
[INFO] processing image 6034/9955
[INFO] processing image 6035/9955
[INFO] processing image 6036/9955
[INFO] processing image 6037/9955
[INFO] processing image 6038/9955
[INFO] processing image 6039/9955
[INFO] processing image 6040/9955
[INFO] processing image 6041/9955
[INFO] processing image 6042/9955
[INFO] processing image 6043/9955
[INFO] processing image 6044/9955
[INFO] processing image 6045/9955
[INFO] processing image 6046/9955
[INFO] processing image 6047/9955
[INFO] processing image 6048/9955
[INFO] processing image 6049/9955
[INFO] processing image 6050/9955
[INFO] processing image 6051/9955
[INFO] processing image 6052/9955
[INFO] processing image 6053/9955
[INFO] processing image 6054/9955
[INFO] processing image 6055/9955
[INFO] processing image 6056/9955
[INFO] processing image 6057/9955
[INFO] processing image 6058/9955
[INFO] processing image 6059/9955
[INFO] processing image 6060/9955
[INFO] processing image 6061/9955
[INFO] processing image 6062/9955
[INFO] processing image 6063/9955
[INFO] processing image 6064/9955
[INFO] processing image 6065/9955
[INFO] processing image 6066/9955
[INFO] processing image 6067/9955
[INFO] processing image 6068/9955
[INFO] processing image 6069/9955
[INFO] processing image 6070/9955
[INFO] processing image 6071/9955
[INFO] processing image 6072/9955
[INFO] processing image 6073/9955
[INFO] processing image 6074/9955
[INFO] processing image 6075/9955
[INFO] processing image 6076/9955
[INFO] processing image 6077/9955
[INFO] processing image 6078/9955
[INFO] processing image 6079/9955
[INFO] processing image 6080/9955
[INFO] processing image 6081/9955
[INFO] processing image 6082/9955
[INFO] processing image 6083/9955
[INFO] processing image 6084/9955
[INFO] processing image 6085/9955
[INFO] processing image 6086/9955
[INFO] processing image 6087/9955
[INFO] processing image 6088/9955
[INFO] processing image 6089/9955
[INFO] processing image 6090/9955
[INFO] processing image 6091/9955
[INFO] processing image 6092/9955
[INFO] processing image 6093/9955
[INFO] processing image 6094/9955
[INFO] processing image 6095/9955
[INFO] processing image 6096/9955
[INFO] processing image 6097/9955
[INFO] processing image 6098/9955
[INFO] processing image 6099/9955
[INFO] processing image 6100/9955
[INFO] processing image 6101/9955
[INFO] processing image 6102/9955
[INFO] processing image 6103/9955
[INFO] processing image 6104/9955
[INFO] processing image 6105/9955
[INFO] processing image 6106/9955
[INFO] processing image 6107/9955
[INFO] processing image 6108/9955
[INFO] processing image 6109/9955
[INFO] processing image 6110/9955
[INFO] processing image 6111/9955
[INFO] processing image 6112/9955
[INFO] processing image 6113/9955
[INFO] processing image 6114/9955
[INFO] processing image 6115/9955
[INFO] processing image 6116/9955
[INFO] processing image 6117/9955
[INFO] processing image 6118/9955
[INFO] processing image 6119/9955
[INFO] processing image 6120/9955
[INFO] processing image 6121/9955
[INFO] processing image 6122/9955
[INFO] processing image 6123/9955
[INFO] processing image 6124/9955
[INFO] processing image 6125/9955
[INFO] processing image 6126/9955
[INFO] processing image 6127/9955
[INFO] processing image 6128/9955
[INFO] processing image 6129/9955
[INFO] processing image 6130/9955
[INFO] processing image 6131/9955
[INFO] processing image 6132/9955
[INFO] processing image 6133/9955
[INFO] processing image 6134/9955
[INFO] processing image 6135/9955
[INFO] processing image 6136/9955
[INFO] processing image 6137/9955
[INFO] processing image 6138/9955
[INFO] processing image 6139/9955
[INFO] processing image 6140/9955
[INFO] processing image 6141/9955
[INFO] processing image 6142/9955
[INFO] processing image 6143/9955
[INFO] processing image 6144/9955
[INFO] processing image 6145/9955
[INFO] processing image 6146/9955
[INFO] processing image 6147/9955
[INFO] processing image 6148/9955
[INFO] processing image 6149/9955
[INFO] processing image 6150/9955
[INFO] processing image 6151/9955
[INFO] processing image 6152/9955
[INFO] processing image 6153/9955
[INFO] processing image 6154/9955
[INFO] processing image 6155/9955
[INFO] processing image 6156/9955
[INFO] processing image 6157/9955
[INFO] processing image 6158/9955
[INFO] processing image 6159/9955
[INFO] processing image 6160/9955
[INFO] processing image 6161/9955
[INFO] processing image 6162/9955
[INFO] processing image 6163/9955
[INFO] processing image 6164/9955
[INFO] processing image 6165/9955
[INFO] processing image 6166/9955
[INFO] processing image 6167/9955
[INFO] processing image 6168/9955
[INFO] processing image 6169/9955
[INFO] processing image 6170/9955
[INFO] processing image 6171/9955
[INFO] processing image 6172/9955
[INFO] processing image 6173/9955
[INFO] processing image 6174/9955
[INFO] processing image 6175/9955
[INFO] processing image 6176/9955
[INFO] processing image 6177/9955
[INFO] processing image 6178/9955
[INFO] processing image 6179/9955
[INFO] processing image 6180/9955
[INFO] processing image 6181/9955
[INFO] processing image 6182/9955
[INFO] processing image 6183/9955
[INFO] processing image 6184/9955
[INFO] processing image 6185/9955
[INFO] processing image 6186/9955
[INFO] processing image 6187/9955
[INFO] processing image 6188/9955
[INFO] processing image 6189/9955
[INFO] processing image 6190/9955
[INFO] processing image 6191/9955
[INFO] processing image 6192/9955
[INFO] processing image 6193/9955
[INFO] processing image 6194/9955
[INFO] processing image 6195/9955
[INFO] processing image 6196/9955
[INFO] processing image 6197/9955
[INFO] processing image 6198/9955
[INFO] processing image 6199/9955
[INFO] processing image 6200/9955
[INFO] processing image 6201/9955
[INFO] processing image 6202/9955
[INFO] processing image 6203/9955
[INFO] processing image 6204/9955
[INFO] processing image 6205/9955
[INFO] processing image 6206/9955
[INFO] processing image 6207/9955
[INFO] processing image 6208/9955
[INFO] processing image 6209/9955
[INFO] processing image 6210/9955
[INFO] processing image 6211/9955
[INFO] processing image 6212/9955
[INFO] processing image 6213/9955
[INFO] processing image 6214/9955
[INFO] processing image 6215/9955
[INFO] processing image 6216/9955
[INFO] processing image 6217/9955
[INFO] processing image 6218/9955
[INFO] processing image 6219/9955
[INFO] processing image 6220/9955
[INFO] processing image 6221/9955
[INFO] processing image 6222/9955
[INFO] processing image 6223/9955
[INFO] processing image 6224/9955
[INFO] processing image 6225/9955
[INFO] processing image 6226/9955
[INFO] processing image 6227/9955
[INFO] processing image 6228/9955
[INFO] processing image 6229/9955
[INFO] processing image 6230/9955
[INFO] processing image 6231/9955
[INFO] processing image 6232/9955
[INFO] processing image 6233/9955
[INFO] processing image 6234/9955
[INFO] processing image 6235/9955
[INFO] processing image 6236/9955
[INFO] processing image 6237/9955
[INFO] processing image 6238/9955
[INFO] processing image 6239/9955
[INFO] processing image 6240/9955
[INFO] processing image 6241/9955
[INFO] processing image 6242/9955
[INFO] processing image 6243/9955
[INFO] processing image 6244/9955
[INFO] processing image 6245/9955
[INFO] processing image 6246/9955
[INFO] processing image 6247/9955
[INFO] processing image 6248/9955
[INFO] processing image 6249/9955
[INFO] processing image 6250/9955
[INFO] processing image 6251/9955
[INFO] processing image 6252/9955
[INFO] processing image 6253/9955
[INFO] processing image 6254/9955
[INFO] processing image 6255/9955
[INFO] processing image 6256/9955
[INFO] processing image 6257/9955
[INFO] processing image 6258/9955
[INFO] processing image 6259/9955
[INFO] processing image 6260/9955
[INFO] processing image 6261/9955
[INFO] processing image 6262/9955
[INFO] processing image 6263/9955
[INFO] processing image 6264/9955
[INFO] processing image 6265/9955
[INFO] processing image 6266/9955
[INFO] processing image 6267/9955
[INFO] processing image 6268/9955
[INFO] processing image 6269/9955
[INFO] processing image 6270/9955
[INFO] processing image 6271/9955
[INFO] processing image 6272/9955
[INFO] processing image 6273/9955
[INFO] processing image 6274/9955
[INFO] processing image 6275/9955
[INFO] processing image 6276/9955
[INFO] processing image 6277/9955
[INFO] processing image 6278/9955
[INFO] processing image 6279/9955
[INFO] processing image 6280/9955
[INFO] processing image 6281/9955
[INFO] processing image 6282/9955
[INFO] processing image 6283/9955
[INFO] processing image 6284/9955
[INFO] processing image 6285/9955
[INFO] processing image 6286/9955
[INFO] processing image 6287/9955
[INFO] processing image 6288/9955
[INFO] processing image 6289/9955
[INFO] processing image 6290/9955
[INFO] processing image 6291/9955
[INFO] processing image 6292/9955
[INFO] processing image 6293/9955
[INFO] processing image 6294/9955
[INFO] processing image 6295/9955
[INFO] processing image 6296/9955
[INFO] processing image 6297/9955
[INFO] processing image 6298/9955
[INFO] processing image 6299/9955
[INFO] processing image 6300/9955
[INFO] processing image 6301/9955
[INFO] processing image 6302/9955
[INFO] processing image 6303/9955
[INFO] processing image 6304/9955
[INFO] processing image 6305/9955
[INFO] processing image 6306/9955
[INFO] processing image 6307/9955
[INFO] processing image 6308/9955
[INFO] processing image 6309/9955
[INFO] processing image 6310/9955
[INFO] processing image 6311/9955
[INFO] processing image 6312/9955
[INFO] processing image 6313/9955
[INFO] processing image 6314/9955
[INFO] processing image 6315/9955
[INFO] processing image 6316/9955
[INFO] processing image 6317/9955
[INFO] processing image 6318/9955
[INFO] processing image 6319/9955
[INFO] processing image 6320/9955
[INFO] processing image 6321/9955
[INFO] processing image 6322/9955
[INFO] processing image 6323/9955
[INFO] processing image 6324/9955
[INFO] processing image 6325/9955
[INFO] processing image 6326/9955
[INFO] processing image 6327/9955
[INFO] processing image 6328/9955
[INFO] processing image 6329/9955
[INFO] processing image 6330/9955
[INFO] processing image 6331/9955
[INFO] processing image 6332/9955
[INFO] processing image 6333/9955
[INFO] processing image 6334/9955
[INFO] processing image 6335/9955
[INFO] processing image 6336/9955
[INFO] processing image 6337/9955
[INFO] processing image 6338/9955
[INFO] processing image 6339/9955
[INFO] processing image 6340/9955
[INFO] processing image 6341/9955
[INFO] processing image 6342/9955
[INFO] processing image 6343/9955
[INFO] processing image 6344/9955
[INFO] processing image 6345/9955
[INFO] processing image 6346/9955
[INFO] processing image 6347/9955
[INFO] processing image 6348/9955
[INFO] processing image 6349/9955
[INFO] processing image 6350/9955
[INFO] processing image 6351/9955
[INFO] processing image 6352/9955
[INFO] processing image 6353/9955
[INFO] processing image 6354/9955
[INFO] processing image 6355/9955
[INFO] processing image 6356/9955
[INFO] processing image 6357/9955
[INFO] processing image 6358/9955
[INFO] processing image 6359/9955
[INFO] processing image 6360/9955
[INFO] processing image 6361/9955
[INFO] processing image 6362/9955
[INFO] processing image 6363/9955
[INFO] processing image 6364/9955
[INFO] processing image 6365/9955
[INFO] processing image 6366/9955
[INFO] processing image 6367/9955
[INFO] processing image 6368/9955
[INFO] processing image 6369/9955
[INFO] processing image 6370/9955
[INFO] processing image 6371/9955
[INFO] processing image 6372/9955
[INFO] processing image 6373/9955
[INFO] processing image 6374/9955
[INFO] processing image 6375/9955
[INFO] processing image 6376/9955
[INFO] processing image 6377/9955
[INFO] processing image 6378/9955
[INFO] processing image 6379/9955
[INFO] processing image 6380/9955
[INFO] processing image 6381/9955
[INFO] processing image 6382/9955
[INFO] processing image 6383/9955
[INFO] processing image 6384/9955
[INFO] processing image 6385/9955
[INFO] processing image 6386/9955
[INFO] processing image 6387/9955
[INFO] processing image 6388/9955
[INFO] processing image 6389/9955
[INFO] processing image 6390/9955
[INFO] processing image 6391/9955
[INFO] processing image 6392/9955
[INFO] processing image 6393/9955
[INFO] processing image 6394/9955
[INFO] processing image 6395/9955
[INFO] processing image 6396/9955
[INFO] processing image 6397/9955
[INFO] processing image 6398/9955
[INFO] processing image 6399/9955
[INFO] processing image 6400/9955
[INFO] processing image 6401/9955
[INFO] processing image 6402/9955
[INFO] processing image 6403/9955
[INFO] processing image 6404/9955
[INFO] processing image 6405/9955
[INFO] processing image 6406/9955
[INFO] processing image 6407/9955
[INFO] processing image 6408/9955
[INFO] processing image 6409/9955
[INFO] processing image 6410/9955
[INFO] processing image 6411/9955
[INFO] processing image 6412/9955
[INFO] processing image 6413/9955
[INFO] processing image 6414/9955
[INFO] processing image 6415/9955
[INFO] processing image 6416/9955
[INFO] processing image 6417/9955
[INFO] processing image 6418/9955
[INFO] processing image 6419/9955
[INFO] processing image 6420/9955
[INFO] processing image 6421/9955
[INFO] processing image 6422/9955
[INFO] processing image 6423/9955
[INFO] processing image 6424/9955
[INFO] processing image 6425/9955
[INFO] processing image 6426/9955
[INFO] processing image 6427/9955
[INFO] processing image 6428/9955
[INFO] processing image 6429/9955
[INFO] processing image 6430/9955
[INFO] processing image 6431/9955
[INFO] processing image 6432/9955
[INFO] processing image 6433/9955
[INFO] processing image 6434/9955
[INFO] processing image 6435/9955
[INFO] processing image 6436/9955
[INFO] processing image 6437/9955
[INFO] processing image 6438/9955
[INFO] processing image 6439/9955
[INFO] processing image 6440/9955
[INFO] processing image 6441/9955
[INFO] processing image 6442/9955
[INFO] processing image 6443/9955
[INFO] processing image 6444/9955
[INFO] processing image 6445/9955
[INFO] processing image 6446/9955
[INFO] processing image 6447/9955
[INFO] processing image 6448/9955
[INFO] processing image 6449/9955
[INFO] processing image 6450/9955
[INFO] processing image 6451/9955
[INFO] processing image 6452/9955
[INFO] processing image 6453/9955
[INFO] processing image 6454/9955
[INFO] processing image 6455/9955
[INFO] processing image 6456/9955
[INFO] processing image 6457/9955
[INFO] processing image 6458/9955
[INFO] processing image 6459/9955
[INFO] processing image 6460/9955
[INFO] processing image 6461/9955
[INFO] processing image 6462/9955
[INFO] processing image 6463/9955
[INFO] processing image 6464/9955
[INFO] processing image 6465/9955
[INFO] processing image 6466/9955
[INFO] processing image 6467/9955
[INFO] processing image 6468/9955
[INFO] processing image 6469/9955
[INFO] processing image 6470/9955
[INFO] processing image 6471/9955
[INFO] processing image 6472/9955
[INFO] processing image 6473/9955
[INFO] processing image 6474/9955
[INFO] processing image 6475/9955
[INFO] processing image 6476/9955
[INFO] processing image 6477/9955
[INFO] processing image 6478/9955
[INFO] processing image 6479/9955
[INFO] processing image 6480/9955
[INFO] processing image 6481/9955
[INFO] processing image 6482/9955
[INFO] processing image 6483/9955
[INFO] processing image 6484/9955
[INFO] processing image 6485/9955
[INFO] processing image 6486/9955
[INFO] processing image 6487/9955
[INFO] processing image 6488/9955
[INFO] processing image 6489/9955
[INFO] processing image 6490/9955
[INFO] processing image 6491/9955
[INFO] processing image 6492/9955
[INFO] processing image 6493/9955
[INFO] processing image 6494/9955
[INFO] processing image 6495/9955
[INFO] processing image 6496/9955
[INFO] processing image 6497/9955
[INFO] processing image 6498/9955
[INFO] processing image 6499/9955
[INFO] processing image 6500/9955
[INFO] processing image 6501/9955
[INFO] processing image 6502/9955
[INFO] processing image 6503/9955
[INFO] processing image 6504/9955
[INFO] processing image 6505/9955
[INFO] processing image 6506/9955
[INFO] processing image 6507/9955
[INFO] processing image 6508/9955
[INFO] processing image 6509/9955
[INFO] processing image 6510/9955
[INFO] processing image 6511/9955
[INFO] processing image 6512/9955
[INFO] processing image 6513/9955
[INFO] processing image 6514/9955
[INFO] processing image 6515/9955
[INFO] processing image 6516/9955
[INFO] processing image 6517/9955
[INFO] processing image 6518/9955
[INFO] processing image 6519/9955
[INFO] processing image 6520/9955
[INFO] processing image 6521/9955
[INFO] processing image 6522/9955
[INFO] processing image 6523/9955
[INFO] processing image 6524/9955
[INFO] processing image 6525/9955
[INFO] processing image 6526/9955
[INFO] processing image 6527/9955
[INFO] processing image 6528/9955
[INFO] processing image 6529/9955
[INFO] processing image 6530/9955
[INFO] processing image 6531/9955
[INFO] processing image 6532/9955
[INFO] processing image 6533/9955
[INFO] processing image 6534/9955
[INFO] processing image 6535/9955
[INFO] processing image 6536/9955
[INFO] processing image 6537/9955
[INFO] processing image 6538/9955
[INFO] processing image 6539/9955
[INFO] processing image 6540/9955
[INFO] processing image 6541/9955
[INFO] processing image 6542/9955
[INFO] processing image 6543/9955
[INFO] processing image 6544/9955
[INFO] processing image 6545/9955
[INFO] processing image 6546/9955
[INFO] processing image 6547/9955
[INFO] processing image 6548/9955
[INFO] processing image 6549/9955
[INFO] processing image 6550/9955
[INFO] processing image 6551/9955
[INFO] processing image 6552/9955
[INFO] processing image 6553/9955
[INFO] processing image 6554/9955
[INFO] processing image 6555/9955
[INFO] processing image 6556/9955
[INFO] processing image 6557/9955
[INFO] processing image 6558/9955
[INFO] processing image 6559/9955
[INFO] processing image 6560/9955
[INFO] processing image 6561/9955
[INFO] processing image 6562/9955
[INFO] processing image 6563/9955
[INFO] processing image 6564/9955
[INFO] processing image 6565/9955
[INFO] processing image 6566/9955
[INFO] processing image 6567/9955
[INFO] processing image 6568/9955
[INFO] processing image 6569/9955
[INFO] processing image 6570/9955
[INFO] processing image 6571/9955
[INFO] processing image 6572/9955
[INFO] processing image 6573/9955
[INFO] processing image 6574/9955
[INFO] processing image 6575/9955
[INFO] processing image 6576/9955
[INFO] processing image 6577/9955
[INFO] processing image 6578/9955
[INFO] processing image 6579/9955
[INFO] processing image 6580/9955
[INFO] processing image 6581/9955
[INFO] processing image 6582/9955
[INFO] processing image 6583/9955
[INFO] processing image 6584/9955
[INFO] processing image 6585/9955
[INFO] processing image 6586/9955
[INFO] processing image 6587/9955
[INFO] processing image 6588/9955
[INFO] processing image 6589/9955
[INFO] processing image 6590/9955
[INFO] processing image 6591/9955
[INFO] processing image 6592/9955
[INFO] processing image 6593/9955
[INFO] processing image 6594/9955
[INFO] processing image 6595/9955
[INFO] processing image 6596/9955
[INFO] processing image 6597/9955
[INFO] processing image 6598/9955
[INFO] processing image 6599/9955
[INFO] processing image 6600/9955
[INFO] processing image 6601/9955
[INFO] processing image 6602/9955
[INFO] processing image 6603/9955
[INFO] processing image 6604/9955
[INFO] processing image 6605/9955
[INFO] processing image 6606/9955
[INFO] processing image 6607/9955
[INFO] processing image 6608/9955
[INFO] processing image 6609/9955
[INFO] processing image 6610/9955
[INFO] processing image 6611/9955
[INFO] processing image 6612/9955
[INFO] processing image 6613/9955
[INFO] processing image 6614/9955
[INFO] processing image 6615/9955
[INFO] processing image 6616/9955
[INFO] processing image 6617/9955
[INFO] processing image 6618/9955
[INFO] processing image 6619/9955
[INFO] processing image 6620/9955
[INFO] processing image 6621/9955
[INFO] processing image 6622/9955
[INFO] processing image 6623/9955
[INFO] processing image 6624/9955
[INFO] processing image 6625/9955
[INFO] processing image 6626/9955
[INFO] processing image 6627/9955
[INFO] processing image 6628/9955
[INFO] processing image 6629/9955
[INFO] processing image 6630/9955
[INFO] processing image 6631/9955
[INFO] processing image 6632/9955
[INFO] processing image 6633/9955
[INFO] processing image 6634/9955
[INFO] processing image 6635/9955
[INFO] processing image 6636/9955
[INFO] processing image 6637/9955
[INFO] processing image 6638/9955
[INFO] processing image 6639/9955
[INFO] processing image 6640/9955
[INFO] processing image 6641/9955
[INFO] processing image 6642/9955
[INFO] processing image 6643/9955
[INFO] processing image 6644/9955
[INFO] processing image 6645/9955
[INFO] processing image 6646/9955
[INFO] processing image 6647/9955
[INFO] processing image 6648/9955
[INFO] processing image 6649/9955
[INFO] processing image 6650/9955
[INFO] processing image 6651/9955
[INFO] processing image 6652/9955
[INFO] processing image 6653/9955
[INFO] processing image 6654/9955
[INFO] processing image 6655/9955
[INFO] processing image 6656/9955
[INFO] processing image 6657/9955
[INFO] processing image 6658/9955
[INFO] processing image 6659/9955
[INFO] processing image 6660/9955
[INFO] processing image 6661/9955
[INFO] processing image 6662/9955
[INFO] processing image 6663/9955
[INFO] processing image 6664/9955
[INFO] processing image 6665/9955
[INFO] processing image 6666/9955
[INFO] processing image 6667/9955
[INFO] processing image 6668/9955
[INFO] processing image 6669/9955
[INFO] processing image 6670/9955
[INFO] processing image 6671/9955
[INFO] processing image 6672/9955
[INFO] processing image 6673/9955
[INFO] processing image 6674/9955
[INFO] processing image 6675/9955
[INFO] processing image 6676/9955
[INFO] processing image 6677/9955
[INFO] processing image 6678/9955
[INFO] processing image 6679/9955
[INFO] processing image 6680/9955
[INFO] processing image 6681/9955
[INFO] processing image 6682/9955
[INFO] processing image 6683/9955
[INFO] processing image 6684/9955
[INFO] processing image 6685/9955
[INFO] processing image 6686/9955
[INFO] processing image 6687/9955
[INFO] processing image 6688/9955
[INFO] processing image 6689/9955
[INFO] processing image 6690/9955
[INFO] processing image 6691/9955
[INFO] processing image 6692/9955
[INFO] processing image 6693/9955
[INFO] processing image 6694/9955
[INFO] processing image 6695/9955
[INFO] processing image 6696/9955
[INFO] processing image 6697/9955
[INFO] processing image 6698/9955
[INFO] processing image 6699/9955
[INFO] processing image 6700/9955
[INFO] processing image 6701/9955
[INFO] processing image 6702/9955
[INFO] processing image 6703/9955
[INFO] processing image 6704/9955
[INFO] processing image 6705/9955
[INFO] processing image 6706/9955
[INFO] processing image 6707/9955
[INFO] processing image 6708/9955
[INFO] processing image 6709/9955
[INFO] processing image 6710/9955
[INFO] processing image 6711/9955
[INFO] processing image 6712/9955
[INFO] processing image 6713/9955
[INFO] processing image 6714/9955
[INFO] processing image 6715/9955
[INFO] processing image 6716/9955
[INFO] processing image 6717/9955
[INFO] processing image 6718/9955
[INFO] processing image 6719/9955
[INFO] processing image 6720/9955
[INFO] processing image 6721/9955
[INFO] processing image 6722/9955
[INFO] processing image 6723/9955
[INFO] processing image 6724/9955
[INFO] processing image 6725/9955
[INFO] processing image 6726/9955
[INFO] processing image 6727/9955
[INFO] processing image 6728/9955
[INFO] processing image 6729/9955
[INFO] processing image 6730/9955
[INFO] processing image 6731/9955
[INFO] processing image 6732/9955
[INFO] processing image 6733/9955
[INFO] processing image 6734/9955
[INFO] processing image 6735/9955
[INFO] processing image 6736/9955
[INFO] processing image 6737/9955
[INFO] processing image 6738/9955
[INFO] processing image 6739/9955
[INFO] processing image 6740/9955
[INFO] processing image 6741/9955
[INFO] processing image 6742/9955
[INFO] processing image 6743/9955
[INFO] processing image 6744/9955
[INFO] processing image 6745/9955
[INFO] processing image 6746/9955
[INFO] processing image 6747/9955
[INFO] processing image 6748/9955
[INFO] processing image 6749/9955
[INFO] processing image 6750/9955
[INFO] processing image 6751/9955
[INFO] processing image 6752/9955
[INFO] processing image 6753/9955
[INFO] processing image 6754/9955
[INFO] processing image 6755/9955
[INFO] processing image 6756/9955
[INFO] processing image 6757/9955
[INFO] processing image 6758/9955
[INFO] processing image 6759/9955
[INFO] processing image 6760/9955
[INFO] processing image 6761/9955
[INFO] processing image 6762/9955
[INFO] processing image 6763/9955
[INFO] processing image 6764/9955
[INFO] processing image 6765/9955
[INFO] processing image 6766/9955
[INFO] processing image 6767/9955
[INFO] processing image 6768/9955
[INFO] processing image 6769/9955
[INFO] processing image 6770/9955
[INFO] processing image 6771/9955
[INFO] processing image 6772/9955
[INFO] processing image 6773/9955
[INFO] processing image 6774/9955
[INFO] processing image 6775/9955
[INFO] processing image 6776/9955
[INFO] processing image 6777/9955
[INFO] processing image 6778/9955
[INFO] processing image 6779/9955
[INFO] processing image 6780/9955
[INFO] processing image 6781/9955
[INFO] processing image 6782/9955
[INFO] processing image 6783/9955
[INFO] processing image 6784/9955
[INFO] processing image 6785/9955
[INFO] processing image 6786/9955
[INFO] processing image 6787/9955
[INFO] processing image 6788/9955
[INFO] processing image 6789/9955
[INFO] processing image 6790/9955
[INFO] processing image 6791/9955
[INFO] processing image 6792/9955
[INFO] processing image 6793/9955
[INFO] processing image 6794/9955
[INFO] processing image 6795/9955
[INFO] processing image 6796/9955
[INFO] processing image 6797/9955
[INFO] processing image 6798/9955
[INFO] processing image 6799/9955
[INFO] processing image 6800/9955
[INFO] processing image 6801/9955
[INFO] processing image 6802/9955
[INFO] processing image 6803/9955
[INFO] processing image 6804/9955
[INFO] processing image 6805/9955
[INFO] processing image 6806/9955
[INFO] processing image 6807/9955
[INFO] processing image 6808/9955
[INFO] processing image 6809/9955
[INFO] processing image 6810/9955
[INFO] processing image 6811/9955
[INFO] processing image 6812/9955
[INFO] processing image 6813/9955
[INFO] processing image 6814/9955
[INFO] processing image 6815/9955
[INFO] processing image 6816/9955
[INFO] processing image 6817/9955
[INFO] processing image 6818/9955
[INFO] processing image 6819/9955
[INFO] processing image 6820/9955
[INFO] processing image 6821/9955
[INFO] processing image 6822/9955
[INFO] processing image 6823/9955
[INFO] processing image 6824/9955
[INFO] processing image 6825/9955
[INFO] processing image 6826/9955
[INFO] processing image 6827/9955
[INFO] processing image 6828/9955
[INFO] processing image 6829/9955
[INFO] processing image 6830/9955
[INFO] processing image 6831/9955
[INFO] processing image 6832/9955
[INFO] processing image 6833/9955
[INFO] processing image 6834/9955
[INFO] processing image 6835/9955
[INFO] processing image 6836/9955
[INFO] processing image 6837/9955
[INFO] processing image 6838/9955
[INFO] processing image 6839/9955
[INFO] processing image 6840/9955
[INFO] processing image 6841/9955
[INFO] processing image 6842/9955
[INFO] processing image 6843/9955
[INFO] processing image 6844/9955
[INFO] processing image 6845/9955
[INFO] processing image 6846/9955
[INFO] processing image 6847/9955
[INFO] processing image 6848/9955
[INFO] processing image 6849/9955
[INFO] processing image 6850/9955
[INFO] processing image 6851/9955
[INFO] processing image 6852/9955
[INFO] processing image 6853/9955
[INFO] processing image 6854/9955
[INFO] processing image 6855/9955
[INFO] processing image 6856/9955
[INFO] processing image 6857/9955
[INFO] processing image 6858/9955
[INFO] processing image 6859/9955
[INFO] processing image 6860/9955
[INFO] processing image 6861/9955
[INFO] processing image 6862/9955
[INFO] processing image 6863/9955
[INFO] processing image 6864/9955
[INFO] processing image 6865/9955
[INFO] processing image 6866/9955
[INFO] processing image 6867/9955
[INFO] processing image 6868/9955
[INFO] processing image 6869/9955
[INFO] processing image 6870/9955
[INFO] processing image 6871/9955
[INFO] processing image 6872/9955
[INFO] processing image 6873/9955
[INFO] processing image 6874/9955
[INFO] processing image 6875/9955
[INFO] processing image 6876/9955
[INFO] processing image 6877/9955
[INFO] processing image 6878/9955
[INFO] processing image 6879/9955
[INFO] processing image 6880/9955
[INFO] processing image 6881/9955
[INFO] processing image 6882/9955
[INFO] processing image 6883/9955
[INFO] processing image 6884/9955
[INFO] processing image 6885/9955
[INFO] processing image 6886/9955
[INFO] processing image 6887/9955
[INFO] processing image 6888/9955
[INFO] processing image 6889/9955
[INFO] processing image 6890/9955
[INFO] processing image 6891/9955
[INFO] processing image 6892/9955
[INFO] processing image 6893/9955
[INFO] processing image 6894/9955
[INFO] processing image 6895/9955
[INFO] processing image 6896/9955
[INFO] processing image 6897/9955
[INFO] processing image 6898/9955
[INFO] processing image 6899/9955
[INFO] processing image 6900/9955
[INFO] processing image 6901/9955
[INFO] processing image 6902/9955
[INFO] processing image 6903/9955
[INFO] processing image 6904/9955
[INFO] processing image 6905/9955
[INFO] processing image 6906/9955
[INFO] processing image 6907/9955
[INFO] processing image 6908/9955
[INFO] processing image 6909/9955
[INFO] processing image 6910/9955
[INFO] processing image 6911/9955
[INFO] processing image 6912/9955
[INFO] processing image 6913/9955
[INFO] processing image 6914/9955
[INFO] processing image 6915/9955
[INFO] processing image 6916/9955
[INFO] processing image 6917/9955
[INFO] processing image 6918/9955
[INFO] processing image 6919/9955
[INFO] processing image 6920/9955
[INFO] processing image 6921/9955
[INFO] processing image 6922/9955
[INFO] processing image 6923/9955
[INFO] processing image 6924/9955
[INFO] processing image 6925/9955
[INFO] processing image 6926/9955
[INFO] processing image 6927/9955
[INFO] processing image 6928/9955
[INFO] processing image 6929/9955
[INFO] processing image 6930/9955
[INFO] processing image 6931/9955
[INFO] processing image 6932/9955
[INFO] processing image 6933/9955
[INFO] processing image 6934/9955
[INFO] processing image 6935/9955
[INFO] processing image 6936/9955
[INFO] processing image 6937/9955
[INFO] processing image 6938/9955
[INFO] processing image 6939/9955
[INFO] processing image 6940/9955
[INFO] processing image 6941/9955
[INFO] processing image 6942/9955
[INFO] processing image 6943/9955
[INFO] processing image 6944/9955
[INFO] processing image 6945/9955
[INFO] processing image 6946/9955
[INFO] processing image 6947/9955
[INFO] processing image 6948/9955
[INFO] processing image 6949/9955
[INFO] processing image 6950/9955
[INFO] processing image 6951/9955
[INFO] processing image 6952/9955
[INFO] processing image 6953/9955
[INFO] processing image 6954/9955
[INFO] processing image 6955/9955
[INFO] processing image 6956/9955
[INFO] processing image 6957/9955
[INFO] processing image 6958/9955
[INFO] processing image 6959/9955
[INFO] processing image 6960/9955
[INFO] processing image 6961/9955
[INFO] processing image 6962/9955
[INFO] processing image 6963/9955
[INFO] processing image 6964/9955
[INFO] processing image 6965/9955
[INFO] processing image 6966/9955
[INFO] processing image 6967/9955
[INFO] processing image 6968/9955
[INFO] processing image 6969/9955
[INFO] processing image 6970/9955
[INFO] processing image 6971/9955
[INFO] processing image 6972/9955
[INFO] processing image 6973/9955
[INFO] processing image 6974/9955
[INFO] processing image 6975/9955
[INFO] processing image 6976/9955
[INFO] processing image 6977/9955
[INFO] processing image 6978/9955
[INFO] processing image 6979/9955
[INFO] processing image 6980/9955
[INFO] processing image 6981/9955
[INFO] processing image 6982/9955
[INFO] processing image 6983/9955
[INFO] processing image 6984/9955
[INFO] processing image 6985/9955
[INFO] processing image 6986/9955
[INFO] processing image 6987/9955
[INFO] processing image 6988/9955
[INFO] processing image 6989/9955
[INFO] processing image 6990/9955
[INFO] processing image 6991/9955
[INFO] processing image 6992/9955
[INFO] processing image 6993/9955
[INFO] processing image 6994/9955
[INFO] processing image 6995/9955
[INFO] processing image 6996/9955
[INFO] processing image 6997/9955
[INFO] processing image 6998/9955
[INFO] processing image 6999/9955
[INFO] processing image 7000/9955
[INFO] processing image 7001/9955
[INFO] processing image 7002/9955
[INFO] processing image 7003/9955
[INFO] processing image 7004/9955
[INFO] processing image 7005/9955
[INFO] processing image 7006/9955
[INFO] processing image 7007/9955
[INFO] processing image 7008/9955
[INFO] processing image 7009/9955
[INFO] processing image 7010/9955
[INFO] processing image 7011/9955
[INFO] processing image 7012/9955
[INFO] processing image 7013/9955
[INFO] processing image 7014/9955
[INFO] processing image 7015/9955
[INFO] processing image 7016/9955
[INFO] processing image 7017/9955
[INFO] processing image 7018/9955
[INFO] processing image 7019/9955
[INFO] processing image 7020/9955
[INFO] processing image 7021/9955
[INFO] processing image 7022/9955
[INFO] processing image 7023/9955
[INFO] processing image 7024/9955
[INFO] processing image 7025/9955
[INFO] processing image 7026/9955
[INFO] processing image 7027/9955
[INFO] processing image 7028/9955
[INFO] processing image 7029/9955
[INFO] processing image 7030/9955
[INFO] processing image 7031/9955
[INFO] processing image 7032/9955
[INFO] processing image 7033/9955
[INFO] processing image 7034/9955
[INFO] processing image 7035/9955
[INFO] processing image 7036/9955
[INFO] processing image 7037/9955
[INFO] processing image 7038/9955
[INFO] processing image 7039/9955
[INFO] processing image 7040/9955
[INFO] processing image 7041/9955
[INFO] processing image 7042/9955
[INFO] processing image 7043/9955
[INFO] processing image 7044/9955
[INFO] processing image 7045/9955
[INFO] processing image 7046/9955
[INFO] processing image 7047/9955
[INFO] processing image 7048/9955
[INFO] processing image 7049/9955
[INFO] processing image 7050/9955
[INFO] processing image 7051/9955
[INFO] processing image 7052/9955
[INFO] processing image 7053/9955
[INFO] processing image 7054/9955
[INFO] processing image 7055/9955
[INFO] processing image 7056/9955
[INFO] processing image 7057/9955
[INFO] processing image 7058/9955
[INFO] processing image 7059/9955
[INFO] processing image 7060/9955
[INFO] processing image 7061/9955
[INFO] processing image 7062/9955
[INFO] processing image 7063/9955
[INFO] processing image 7064/9955
[INFO] processing image 7065/9955
[INFO] processing image 7066/9955
[INFO] processing image 7067/9955
[INFO] processing image 7068/9955
[INFO] processing image 7069/9955
[INFO] processing image 7070/9955
[INFO] processing image 7071/9955
[INFO] processing image 7072/9955
[INFO] processing image 7073/9955
[INFO] processing image 7074/9955
[INFO] processing image 7075/9955
[INFO] processing image 7076/9955
[INFO] processing image 7077/9955
[INFO] processing image 7078/9955
[INFO] processing image 7079/9955
[INFO] processing image 7080/9955
[INFO] processing image 7081/9955
[INFO] processing image 7082/9955
[INFO] processing image 7083/9955
[INFO] processing image 7084/9955
[INFO] processing image 7085/9955
[INFO] processing image 7086/9955
[INFO] processing image 7087/9955
[INFO] processing image 7088/9955
[INFO] processing image 7089/9955
[INFO] processing image 7090/9955
[INFO] processing image 7091/9955
[INFO] processing image 7092/9955
[INFO] processing image 7093/9955
[INFO] processing image 7094/9955
[INFO] processing image 7095/9955
[INFO] processing image 7096/9955
[INFO] processing image 7097/9955
[INFO] processing image 7098/9955
[INFO] processing image 7099/9955
[INFO] processing image 7100/9955
[INFO] processing image 7101/9955
[INFO] processing image 7102/9955
[INFO] processing image 7103/9955
[INFO] processing image 7104/9955
[INFO] processing image 7105/9955
[INFO] processing image 7106/9955
[INFO] processing image 7107/9955
[INFO] processing image 7108/9955
[INFO] processing image 7109/9955
[INFO] processing image 7110/9955
[INFO] processing image 7111/9955
[INFO] processing image 7112/9955
[INFO] processing image 7113/9955
[INFO] processing image 7114/9955
[INFO] processing image 7115/9955
[INFO] processing image 7116/9955
[INFO] processing image 7117/9955
[INFO] processing image 7118/9955
[INFO] processing image 7119/9955
[INFO] processing image 7120/9955
[INFO] processing image 7121/9955
[INFO] processing image 7122/9955
[INFO] processing image 7123/9955
[INFO] processing image 7124/9955
[INFO] processing image 7125/9955
[INFO] processing image 7126/9955
[INFO] processing image 7127/9955
[INFO] processing image 7128/9955
[INFO] processing image 7129/9955
[INFO] processing image 7130/9955
[INFO] processing image 7131/9955
[INFO] processing image 7132/9955
[INFO] processing image 7133/9955
[INFO] processing image 7134/9955
[INFO] processing image 7135/9955
[INFO] processing image 7136/9955
[INFO] processing image 7137/9955
[INFO] processing image 7138/9955
[INFO] processing image 7139/9955
[INFO] processing image 7140/9955
[INFO] processing image 7141/9955
[INFO] processing image 7142/9955
[INFO] processing image 7143/9955
[INFO] processing image 7144/9955
[INFO] processing image 7145/9955
[INFO] processing image 7146/9955
[INFO] processing image 7147/9955
[INFO] processing image 7148/9955
[INFO] processing image 7149/9955
[INFO] processing image 7150/9955
[INFO] processing image 7151/9955
[INFO] processing image 7152/9955
[INFO] processing image 7153/9955
[INFO] processing image 7154/9955
[INFO] processing image 7155/9955
[INFO] processing image 7156/9955
[INFO] processing image 7157/9955
[INFO] processing image 7158/9955
[INFO] processing image 7159/9955
[INFO] processing image 7160/9955
[INFO] processing image 7161/9955
[INFO] processing image 7162/9955
[INFO] processing image 7163/9955
[INFO] processing image 7164/9955
[INFO] processing image 7165/9955
[INFO] processing image 7166/9955
[INFO] processing image 7167/9955
[INFO] processing image 7168/9955
[INFO] processing image 7169/9955
[INFO] processing image 7170/9955
[INFO] processing image 7171/9955
[INFO] processing image 7172/9955
[INFO] processing image 7173/9955
[INFO] processing image 7174/9955
[INFO] processing image 7175/9955
[INFO] processing image 7176/9955
[INFO] processing image 7177/9955
[INFO] processing image 7178/9955
[INFO] processing image 7179/9955
[INFO] processing image 7180/9955
[INFO] processing image 7181/9955
[INFO] processing image 7182/9955
[INFO] processing image 7183/9955
[INFO] processing image 7184/9955
[INFO] processing image 7185/9955
[INFO] processing image 7186/9955
[INFO] processing image 7187/9955
[INFO] processing image 7188/9955
[INFO] processing image 7189/9955
[INFO] processing image 7190/9955
[INFO] processing image 7191/9955
[INFO] processing image 7192/9955
[INFO] processing image 7193/9955
[INFO] processing image 7194/9955
[INFO] processing image 7195/9955
[INFO] processing image 7196/9955
[INFO] processing image 7197/9955
[INFO] processing image 7198/9955
[INFO] processing image 7199/9955
[INFO] processing image 7200/9955
[INFO] processing image 7201/9955
[INFO] processing image 7202/9955
[INFO] processing image 7203/9955
[INFO] processing image 7204/9955
[INFO] processing image 7205/9955
[INFO] processing image 7206/9955
[INFO] processing image 7207/9955
[INFO] processing image 7208/9955
[INFO] processing image 7209/9955
[INFO] processing image 7210/9955
[INFO] processing image 7211/9955
[INFO] processing image 7212/9955
[INFO] processing image 7213/9955
[INFO] processing image 7214/9955
[INFO] processing image 7215/9955
[INFO] processing image 7216/9955
[INFO] processing image 7217/9955
[INFO] processing image 7218/9955
[INFO] processing image 7219/9955
[INFO] processing image 7220/9955
[INFO] processing image 7221/9955
[INFO] processing image 7222/9955
[INFO] processing image 7223/9955
[INFO] processing image 7224/9955
[INFO] processing image 7225/9955
[INFO] processing image 7226/9955
[INFO] processing image 7227/9955
[INFO] processing image 7228/9955
[INFO] processing image 7229/9955
[INFO] processing image 7230/9955
[INFO] processing image 7231/9955
[INFO] processing image 7232/9955
[INFO] processing image 7233/9955
[INFO] processing image 7234/9955
[INFO] processing image 7235/9955
[INFO] processing image 7236/9955
[INFO] processing image 7237/9955
[INFO] processing image 7238/9955
[INFO] processing image 7239/9955
[INFO] processing image 7240/9955
[INFO] processing image 7241/9955
[INFO] processing image 7242/9955
[INFO] processing image 7243/9955
[INFO] processing image 7244/9955
[INFO] processing image 7245/9955
[INFO] processing image 7246/9955
[INFO] processing image 7247/9955
[INFO] processing image 7248/9955
[INFO] processing image 7249/9955
[INFO] processing image 7250/9955
[INFO] processing image 7251/9955
[INFO] processing image 7252/9955
[INFO] processing image 7253/9955
[INFO] processing image 7254/9955
[INFO] processing image 7255/9955
[INFO] processing image 7256/9955
[INFO] processing image 7257/9955
[INFO] processing image 7258/9955
[INFO] processing image 7259/9955
[INFO] processing image 7260/9955
[INFO] processing image 7261/9955
[INFO] processing image 7262/9955
[INFO] processing image 7263/9955
[INFO] processing image 7264/9955
[INFO] processing image 7265/9955
[INFO] processing image 7266/9955
[INFO] processing image 7267/9955
[INFO] processing image 7268/9955
[INFO] processing image 7269/9955
[INFO] processing image 7270/9955
[INFO] processing image 7271/9955
[INFO] processing image 7272/9955
[INFO] processing image 7273/9955
[INFO] processing image 7274/9955
[INFO] processing image 7275/9955
[INFO] processing image 7276/9955
[INFO] processing image 7277/9955
[INFO] processing image 7278/9955
[INFO] processing image 7279/9955
[INFO] processing image 7280/9955
[INFO] processing image 7281/9955
[INFO] processing image 7282/9955
[INFO] processing image 7283/9955
[INFO] processing image 7284/9955
[INFO] processing image 7285/9955
[INFO] processing image 7286/9955
[INFO] processing image 7287/9955
[INFO] processing image 7288/9955
[INFO] processing image 7289/9955
[INFO] processing image 7290/9955
[INFO] processing image 7291/9955
[INFO] processing image 7292/9955
[INFO] processing image 7293/9955
[INFO] processing image 7294/9955
[INFO] processing image 7295/9955
[INFO] processing image 7296/9955
[INFO] processing image 7297/9955
[INFO] processing image 7298/9955
[INFO] processing image 7299/9955
[INFO] processing image 7300/9955
[INFO] processing image 7301/9955
[INFO] processing image 7302/9955
[INFO] processing image 7303/9955
[INFO] processing image 7304/9955
[INFO] processing image 7305/9955
[INFO] processing image 7306/9955
[INFO] processing image 7307/9955
[INFO] processing image 7308/9955
[INFO] processing image 7309/9955
[INFO] processing image 7310/9955
[INFO] processing image 7311/9955
[INFO] processing image 7312/9955
[INFO] processing image 7313/9955
[INFO] processing image 7314/9955
[INFO] processing image 7315/9955
[INFO] processing image 7316/9955
[INFO] processing image 7317/9955
[INFO] processing image 7318/9955
[INFO] processing image 7319/9955
[INFO] processing image 7320/9955
[INFO] processing image 7321/9955
[INFO] processing image 7322/9955
[INFO] processing image 7323/9955
[INFO] processing image 7324/9955
[INFO] processing image 7325/9955
[INFO] processing image 7326/9955
[INFO] processing image 7327/9955
[INFO] processing image 7328/9955
[INFO] processing image 7329/9955
[INFO] processing image 7330/9955
[INFO] processing image 7331/9955
[INFO] processing image 7332/9955
[INFO] processing image 7333/9955
[INFO] processing image 7334/9955
[INFO] processing image 7335/9955
[INFO] processing image 7336/9955
[INFO] processing image 7337/9955
[INFO] processing image 7338/9955
[INFO] processing image 7339/9955
[INFO] processing image 7340/9955
[INFO] processing image 7341/9955
[INFO] processing image 7342/9955
[INFO] processing image 7343/9955
[INFO] processing image 7344/9955
[INFO] processing image 7345/9955
[INFO] processing image 7346/9955
[INFO] processing image 7347/9955
[INFO] processing image 7348/9955
[INFO] processing image 7349/9955
[INFO] processing image 7350/9955
[INFO] processing image 7351/9955
[INFO] processing image 7352/9955
[INFO] processing image 7353/9955
[INFO] processing image 7354/9955
[INFO] processing image 7355/9955
[INFO] processing image 7356/9955
[INFO] processing image 7357/9955
[INFO] processing image 7358/9955
[INFO] processing image 7359/9955
[INFO] processing image 7360/9955
[INFO] processing image 7361/9955
[INFO] processing image 7362/9955
[INFO] processing image 7363/9955
[INFO] processing image 7364/9955
[INFO] processing image 7365/9955
[INFO] processing image 7366/9955
[INFO] processing image 7367/9955
[INFO] processing image 7368/9955
[INFO] processing image 7369/9955
[INFO] processing image 7370/9955
[INFO] processing image 7371/9955
[INFO] processing image 7372/9955
[INFO] processing image 7373/9955
[INFO] processing image 7374/9955
[INFO] processing image 7375/9955
[INFO] processing image 7376/9955
[INFO] processing image 7377/9955
[INFO] processing image 7378/9955
[INFO] processing image 7379/9955
[INFO] processing image 7380/9955
[INFO] processing image 7381/9955
[INFO] processing image 7382/9955
[INFO] processing image 7383/9955
[INFO] processing image 7384/9955
[INFO] processing image 7385/9955
[INFO] processing image 7386/9955
[INFO] processing image 7387/9955
[INFO] processing image 7388/9955
[INFO] processing image 7389/9955
[INFO] processing image 7390/9955
[INFO] processing image 7391/9955
[INFO] processing image 7392/9955
[INFO] processing image 7393/9955
[INFO] processing image 7394/9955
[INFO] processing image 7395/9955
[INFO] processing image 7396/9955
[INFO] processing image 7397/9955
[INFO] processing image 7398/9955
[INFO] processing image 7399/9955
[INFO] processing image 7400/9955
[INFO] processing image 7401/9955
[INFO] processing image 7402/9955
[INFO] processing image 7403/9955
[INFO] processing image 7404/9955
[INFO] processing image 7405/9955
[INFO] processing image 7406/9955
[INFO] processing image 7407/9955
[INFO] processing image 7408/9955
[INFO] processing image 7409/9955
[INFO] processing image 7410/9955
[INFO] processing image 7411/9955
[INFO] processing image 7412/9955
[INFO] processing image 7413/9955
[INFO] processing image 7414/9955
[INFO] processing image 7415/9955
[INFO] processing image 7416/9955
[INFO] processing image 7417/9955
[INFO] processing image 7418/9955
[INFO] processing image 7419/9955
[INFO] processing image 7420/9955
[INFO] processing image 7421/9955
[INFO] processing image 7422/9955
[INFO] processing image 7423/9955
[INFO] processing image 7424/9955
[INFO] processing image 7425/9955
[INFO] processing image 7426/9955
[INFO] processing image 7427/9955
[INFO] processing image 7428/9955
[INFO] processing image 7429/9955
[INFO] processing image 7430/9955
[INFO] processing image 7431/9955
[INFO] processing image 7432/9955
[INFO] processing image 7433/9955
[INFO] processing image 7434/9955
[INFO] processing image 7435/9955
[INFO] processing image 7436/9955
[INFO] processing image 7437/9955
[INFO] processing image 7438/9955
[INFO] processing image 7439/9955
[INFO] processing image 7440/9955
[INFO] processing image 7441/9955
[INFO] processing image 7442/9955
[INFO] processing image 7443/9955
[INFO] processing image 7444/9955
[INFO] processing image 7445/9955
[INFO] processing image 7446/9955
[INFO] processing image 7447/9955
[INFO] processing image 7448/9955
[INFO] processing image 7449/9955
[INFO] processing image 7450/9955
[INFO] processing image 7451/9955
[INFO] processing image 7452/9955
[INFO] processing image 7453/9955
[INFO] processing image 7454/9955
[INFO] processing image 7455/9955
[INFO] processing image 7456/9955
[INFO] processing image 7457/9955
[INFO] processing image 7458/9955
[INFO] processing image 7459/9955
[INFO] processing image 7460/9955
[INFO] processing image 7461/9955
[INFO] processing image 7462/9955
[INFO] processing image 7463/9955
[INFO] processing image 7464/9955
[INFO] processing image 7465/9955
[INFO] processing image 7466/9955
[INFO] processing image 7467/9955
[INFO] processing image 7468/9955
[INFO] processing image 7469/9955
[INFO] processing image 7470/9955
[INFO] processing image 7471/9955
[INFO] processing image 7472/9955
[INFO] processing image 7473/9955
[INFO] processing image 7474/9955
[INFO] processing image 7475/9955
[INFO] processing image 7476/9955
[INFO] processing image 7477/9955
[INFO] processing image 7478/9955
[INFO] processing image 7479/9955
[INFO] processing image 7480/9955
[INFO] processing image 7481/9955
[INFO] processing image 7482/9955
[INFO] processing image 7483/9955
[INFO] processing image 7484/9955
[INFO] processing image 7485/9955
[INFO] processing image 7486/9955
[INFO] processing image 7487/9955
[INFO] processing image 7488/9955
[INFO] processing image 7489/9955
[INFO] processing image 7490/9955
[INFO] processing image 7491/9955
[INFO] processing image 7492/9955
[INFO] processing image 7493/9955
[INFO] processing image 7494/9955
[INFO] processing image 7495/9955
[INFO] processing image 7496/9955
[INFO] processing image 7497/9955
[INFO] processing image 7498/9955
[INFO] processing image 7499/9955
[INFO] processing image 7500/9955
[INFO] processing image 7501/9955
[INFO] processing image 7502/9955
[INFO] processing image 7503/9955
[INFO] processing image 7504/9955
[INFO] processing image 7505/9955
[INFO] processing image 7506/9955
[INFO] processing image 7507/9955
[INFO] processing image 7508/9955
[INFO] processing image 7509/9955
[INFO] processing image 7510/9955
[INFO] processing image 7511/9955
[INFO] processing image 7512/9955
[INFO] processing image 7513/9955
[INFO] processing image 7514/9955
[INFO] processing image 7515/9955
[INFO] processing image 7516/9955
[INFO] processing image 7517/9955
[INFO] processing image 7518/9955
[INFO] processing image 7519/9955
[INFO] processing image 7520/9955
[INFO] processing image 7521/9955
[INFO] processing image 7522/9955
[INFO] processing image 7523/9955
[INFO] processing image 7524/9955
[INFO] processing image 7525/9955
[INFO] processing image 7526/9955
[INFO] processing image 7527/9955
[INFO] processing image 7528/9955
[INFO] processing image 7529/9955
[INFO] processing image 7530/9955
[INFO] processing image 7531/9955
[INFO] processing image 7532/9955
[INFO] processing image 7533/9955
[INFO] processing image 7534/9955
[INFO] processing image 7535/9955
[INFO] processing image 7536/9955
[INFO] processing image 7537/9955
[INFO] processing image 7538/9955
[INFO] processing image 7539/9955
[INFO] processing image 7540/9955
[INFO] processing image 7541/9955
[INFO] processing image 7542/9955
[INFO] processing image 7543/9955
[INFO] processing image 7544/9955
[INFO] processing image 7545/9955
[INFO] processing image 7546/9955
[INFO] processing image 7547/9955
[INFO] processing image 7548/9955
[INFO] processing image 7549/9955
[INFO] processing image 7550/9955
[INFO] processing image 7551/9955
[INFO] processing image 7552/9955
[INFO] processing image 7553/9955
[INFO] processing image 7554/9955
[INFO] processing image 7555/9955
[INFO] processing image 7556/9955
[INFO] processing image 7557/9955
[INFO] processing image 7558/9955
[INFO] processing image 7559/9955
[INFO] processing image 7560/9955
[INFO] processing image 7561/9955
[INFO] processing image 7562/9955
[INFO] processing image 7563/9955
[INFO] processing image 7564/9955
[INFO] processing image 7565/9955
[INFO] processing image 7566/9955
[INFO] processing image 7567/9955
[INFO] processing image 7568/9955
[INFO] processing image 7569/9955
[INFO] processing image 7570/9955
[INFO] processing image 7571/9955
[INFO] processing image 7572/9955
[INFO] processing image 7573/9955
[INFO] processing image 7574/9955
[INFO] processing image 7575/9955
[INFO] processing image 7576/9955
[INFO] processing image 7577/9955
[INFO] processing image 7578/9955
[INFO] processing image 7579/9955
[INFO] processing image 7580/9955
[INFO] processing image 7581/9955
[INFO] processing image 7582/9955
[INFO] processing image 7583/9955
[INFO] processing image 7584/9955
[INFO] processing image 7585/9955
[INFO] processing image 7586/9955
[INFO] processing image 7587/9955
[INFO] processing image 7588/9955
[INFO] processing image 7589/9955
[INFO] processing image 7590/9955
[INFO] processing image 7591/9955
[INFO] processing image 7592/9955
[INFO] processing image 7593/9955
[INFO] processing image 7594/9955
[INFO] processing image 7595/9955
[INFO] processing image 7596/9955
[INFO] processing image 7597/9955
[INFO] processing image 7598/9955
[INFO] processing image 7599/9955
[INFO] processing image 7600/9955
[INFO] processing image 7601/9955
[INFO] processing image 7602/9955
[INFO] processing image 7603/9955
[INFO] processing image 7604/9955
[INFO] processing image 7605/9955
[INFO] processing image 7606/9955
[INFO] processing image 7607/9955
[INFO] processing image 7608/9955
[INFO] processing image 7609/9955
[INFO] processing image 7610/9955
[INFO] processing image 7611/9955
[INFO] processing image 7612/9955
[INFO] processing image 7613/9955
[INFO] processing image 7614/9955
[INFO] processing image 7615/9955
[INFO] processing image 7616/9955
[INFO] processing image 7617/9955
[INFO] processing image 7618/9955
[INFO] processing image 7619/9955
[INFO] processing image 7620/9955
[INFO] processing image 7621/9955
[INFO] processing image 7622/9955
[INFO] processing image 7623/9955
[INFO] processing image 7624/9955
[INFO] processing image 7625/9955
[INFO] processing image 7626/9955
[INFO] processing image 7627/9955
[INFO] processing image 7628/9955
[INFO] processing image 7629/9955
[INFO] processing image 7630/9955
[INFO] processing image 7631/9955
[INFO] processing image 7632/9955
[INFO] processing image 7633/9955
[INFO] processing image 7634/9955
[INFO] processing image 7635/9955
[INFO] processing image 7636/9955
[INFO] processing image 7637/9955
[INFO] processing image 7638/9955
[INFO] processing image 7639/9955
[INFO] processing image 7640/9955
[INFO] processing image 7641/9955
[INFO] processing image 7642/9955
[INFO] processing image 7643/9955
[INFO] processing image 7644/9955
[INFO] processing image 7645/9955
[INFO] processing image 7646/9955
[INFO] processing image 7647/9955
[INFO] processing image 7648/9955
[INFO] processing image 7649/9955
[INFO] processing image 7650/9955
[INFO] processing image 7651/9955
[INFO] processing image 7652/9955
[INFO] processing image 7653/9955
[INFO] processing image 7654/9955
[INFO] processing image 7655/9955
[INFO] processing image 7656/9955
[INFO] processing image 7657/9955
[INFO] processing image 7658/9955
[INFO] processing image 7659/9955
[INFO] processing image 7660/9955
[INFO] processing image 7661/9955
[INFO] processing image 7662/9955
[INFO] processing image 7663/9955
[INFO] processing image 7664/9955
[INFO] processing image 7665/9955
[INFO] processing image 7666/9955
[INFO] processing image 7667/9955
[INFO] processing image 7668/9955
[INFO] processing image 7669/9955
[INFO] processing image 7670/9955
[INFO] processing image 7671/9955
[INFO] processing image 7672/9955
[INFO] processing image 7673/9955
[INFO] processing image 7674/9955
[INFO] processing image 7675/9955
[INFO] processing image 7676/9955
[INFO] processing image 7677/9955
[INFO] processing image 7678/9955
[INFO] processing image 7679/9955
[INFO] processing image 7680/9955
[INFO] processing image 7681/9955
[INFO] processing image 7682/9955
[INFO] processing image 7683/9955
[INFO] processing image 7684/9955
[INFO] processing image 7685/9955
[INFO] processing image 7686/9955
[INFO] processing image 7687/9955
[INFO] processing image 7688/9955
[INFO] processing image 7689/9955
[INFO] processing image 7690/9955
[INFO] processing image 7691/9955
[INFO] processing image 7692/9955
[INFO] processing image 7693/9955
[INFO] processing image 7694/9955
[INFO] processing image 7695/9955
[INFO] processing image 7696/9955
[INFO] processing image 7697/9955
[INFO] processing image 7698/9955
[INFO] processing image 7699/9955
[INFO] processing image 7700/9955
[INFO] processing image 7701/9955
[INFO] processing image 7702/9955
[INFO] processing image 7703/9955
[INFO] processing image 7704/9955
[INFO] processing image 7705/9955
[INFO] processing image 7706/9955
[INFO] processing image 7707/9955
[INFO] processing image 7708/9955
[INFO] processing image 7709/9955
[INFO] processing image 7710/9955
[INFO] processing image 7711/9955
[INFO] processing image 7712/9955
[INFO] processing image 7713/9955
[INFO] processing image 7714/9955
[INFO] processing image 7715/9955
[INFO] processing image 7716/9955
[INFO] processing image 7717/9955
[INFO] processing image 7718/9955
[INFO] processing image 7719/9955
[INFO] processing image 7720/9955
[INFO] processing image 7721/9955
[INFO] processing image 7722/9955
[INFO] processing image 7723/9955
[INFO] processing image 7724/9955
[INFO] processing image 7725/9955
[INFO] processing image 7726/9955
[INFO] processing image 7727/9955
[INFO] processing image 7728/9955
[INFO] processing image 7729/9955
[INFO] processing image 7730/9955
[INFO] processing image 7731/9955
[INFO] processing image 7732/9955
[INFO] processing image 7733/9955
[INFO] processing image 7734/9955
[INFO] processing image 7735/9955
[INFO] processing image 7736/9955
[INFO] processing image 7737/9955
[INFO] processing image 7738/9955
[INFO] processing image 7739/9955
[INFO] processing image 7740/9955
[INFO] processing image 7741/9955
[INFO] processing image 7742/9955
[INFO] processing image 7743/9955
[INFO] processing image 7744/9955
[INFO] processing image 7745/9955
[INFO] processing image 7746/9955
[INFO] processing image 7747/9955
[INFO] processing image 7748/9955
[INFO] processing image 7749/9955
[INFO] processing image 7750/9955
[INFO] processing image 7751/9955
[INFO] processing image 7752/9955
[INFO] processing image 7753/9955
[INFO] processing image 7754/9955
[INFO] processing image 7755/9955
[INFO] processing image 7756/9955
[INFO] processing image 7757/9955
[INFO] processing image 7758/9955
[INFO] processing image 7759/9955
[INFO] processing image 7760/9955
[INFO] processing image 7761/9955
[INFO] processing image 7762/9955
[INFO] processing image 7763/9955
[INFO] processing image 7764/9955
[INFO] processing image 7765/9955
[INFO] processing image 7766/9955
[INFO] processing image 7767/9955
[INFO] processing image 7768/9955
[INFO] processing image 7769/9955
[INFO] processing image 7770/9955
[INFO] processing image 7771/9955
[INFO] processing image 7772/9955
[INFO] processing image 7773/9955
[INFO] processing image 7774/9955
[INFO] processing image 7775/9955
[INFO] processing image 7776/9955
[INFO] processing image 7777/9955
[INFO] processing image 7778/9955
[INFO] processing image 7779/9955
[INFO] processing image 7780/9955
[INFO] processing image 7781/9955
[INFO] processing image 7782/9955
[INFO] processing image 7783/9955
[INFO] processing image 7784/9955
[INFO] processing image 7785/9955
[INFO] processing image 7786/9955
[INFO] processing image 7787/9955
[INFO] processing image 7788/9955
[INFO] processing image 7789/9955
[INFO] processing image 7790/9955
[INFO] processing image 7791/9955
[INFO] processing image 7792/9955
[INFO] processing image 7793/9955
[INFO] processing image 7794/9955
[INFO] processing image 7795/9955
[INFO] processing image 7796/9955
[INFO] processing image 7797/9955
[INFO] processing image 7798/9955
[INFO] processing image 7799/9955
[INFO] processing image 7800/9955
[INFO] processing image 7801/9955
[INFO] processing image 7802/9955
[INFO] processing image 7803/9955
[INFO] processing image 7804/9955
[INFO] processing image 7805/9955
[INFO] processing image 7806/9955
[INFO] processing image 7807/9955
[INFO] processing image 7808/9955
[INFO] processing image 7809/9955
[INFO] processing image 7810/9955
[INFO] processing image 7811/9955
[INFO] processing image 7812/9955
[INFO] processing image 7813/9955
[INFO] processing image 7814/9955
[INFO] processing image 7815/9955
[INFO] processing image 7816/9955
[INFO] processing image 7817/9955
[INFO] processing image 7818/9955
[INFO] processing image 7819/9955
[INFO] processing image 7820/9955
[INFO] processing image 7821/9955
[INFO] processing image 7822/9955
[INFO] processing image 7823/9955
[INFO] processing image 7824/9955
[INFO] processing image 7825/9955
[INFO] processing image 7826/9955
[INFO] processing image 7827/9955
[INFO] processing image 7828/9955
[INFO] processing image 7829/9955
[INFO] processing image 7830/9955
[INFO] processing image 7831/9955
[INFO] processing image 7832/9955
[INFO] processing image 7833/9955
[INFO] processing image 7834/9955
[INFO] processing image 7835/9955
[INFO] processing image 7836/9955
[INFO] processing image 7837/9955
[INFO] processing image 7838/9955
[INFO] processing image 7839/9955
[INFO] processing image 7840/9955
[INFO] processing image 7841/9955
[INFO] processing image 7842/9955
[INFO] processing image 7843/9955
[INFO] processing image 7844/9955
[INFO] processing image 7845/9955
[INFO] processing image 7846/9955
[INFO] processing image 7847/9955
[INFO] processing image 7848/9955
[INFO] processing image 7849/9955
[INFO] processing image 7850/9955
[INFO] processing image 7851/9955
[INFO] processing image 7852/9955
[INFO] processing image 7853/9955
[INFO] processing image 7854/9955
[INFO] processing image 7855/9955
[INFO] processing image 7856/9955
[INFO] processing image 7857/9955
[INFO] processing image 7858/9955
[INFO] processing image 7859/9955
[INFO] processing image 7860/9955
[INFO] processing image 7861/9955
[INFO] processing image 7862/9955
[INFO] processing image 7863/9955
[INFO] processing image 7864/9955
[INFO] processing image 7865/9955
[INFO] processing image 7866/9955
[INFO] processing image 7867/9955
[INFO] processing image 7868/9955
[INFO] processing image 7869/9955
[INFO] processing image 7870/9955
[INFO] processing image 7871/9955
[INFO] processing image 7872/9955
[INFO] processing image 7873/9955
[INFO] processing image 7874/9955
[INFO] processing image 7875/9955
[INFO] processing image 7876/9955
[INFO] processing image 7877/9955
[INFO] processing image 7878/9955
[INFO] processing image 7879/9955
[INFO] processing image 7880/9955
[INFO] processing image 7881/9955
[INFO] processing image 7882/9955
[INFO] processing image 7883/9955
[INFO] processing image 7884/9955
[INFO] processing image 7885/9955
[INFO] processing image 7886/9955
[INFO] processing image 7887/9955
[INFO] processing image 7888/9955
[INFO] processing image 7889/9955
[INFO] processing image 7890/9955
[INFO] processing image 7891/9955
[INFO] processing image 7892/9955
[INFO] processing image 7893/9955
[INFO] processing image 7894/9955
[INFO] processing image 7895/9955
[INFO] processing image 7896/9955
[INFO] processing image 7897/9955
[INFO] processing image 7898/9955
[INFO] processing image 7899/9955
[INFO] processing image 7900/9955
[INFO] processing image 7901/9955
[INFO] processing image 7902/9955
[INFO] processing image 7903/9955
[INFO] processing image 7904/9955
[INFO] processing image 7905/9955
[INFO] processing image 7906/9955
[INFO] processing image 7907/9955
[INFO] processing image 7908/9955
[INFO] processing image 7909/9955
[INFO] processing image 7910/9955
[INFO] processing image 7911/9955
[INFO] processing image 7912/9955
[INFO] processing image 7913/9955
[INFO] processing image 7914/9955
[INFO] processing image 7915/9955
[INFO] processing image 7916/9955
[INFO] processing image 7917/9955
[INFO] processing image 7918/9955
[INFO] processing image 7919/9955
[INFO] processing image 7920/9955
[INFO] processing image 7921/9955
[INFO] processing image 7922/9955
[INFO] processing image 7923/9955
[INFO] processing image 7924/9955
[INFO] processing image 7925/9955
[INFO] processing image 7926/9955
[INFO] processing image 7927/9955
[INFO] processing image 7928/9955
[INFO] processing image 7929/9955
[INFO] processing image 7930/9955
[INFO] processing image 7931/9955
[INFO] processing image 7932/9955
[INFO] processing image 7933/9955
[INFO] processing image 7934/9955
[INFO] processing image 7935/9955
[INFO] processing image 7936/9955
[INFO] processing image 7937/9955
[INFO] processing image 7938/9955
[INFO] processing image 7939/9955
[INFO] processing image 7940/9955
[INFO] processing image 7941/9955
[INFO] processing image 7942/9955
[INFO] processing image 7943/9955
[INFO] processing image 7944/9955
[INFO] processing image 7945/9955
[INFO] processing image 7946/9955
[INFO] processing image 7947/9955
[INFO] processing image 7948/9955
[INFO] processing image 7949/9955
[INFO] processing image 7950/9955
[INFO] processing image 7951/9955
[INFO] processing image 7952/9955
[INFO] processing image 7953/9955
[INFO] processing image 7954/9955
[INFO] processing image 7955/9955
[INFO] processing image 7956/9955
[INFO] processing image 7957/9955
[INFO] processing image 7958/9955
[INFO] processing image 7959/9955
[INFO] processing image 7960/9955
[INFO] processing image 7961/9955
[INFO] processing image 7962/9955
[INFO] processing image 7963/9955
[INFO] processing image 7964/9955
[INFO] processing image 7965/9955
[INFO] processing image 7966/9955
[INFO] processing image 7967/9955
[INFO] processing image 7968/9955
[INFO] processing image 7969/9955
[INFO] processing image 7970/9955
[INFO] processing image 7971/9955
[INFO] processing image 7972/9955
[INFO] processing image 7973/9955
[INFO] processing image 7974/9955
[INFO] processing image 7975/9955
[INFO] processing image 7976/9955
[INFO] processing image 7977/9955
[INFO] processing image 7978/9955
[INFO] processing image 7979/9955
[INFO] processing image 7980/9955
[INFO] processing image 7981/9955
[INFO] processing image 7982/9955
[INFO] processing image 7983/9955
[INFO] processing image 7984/9955
[INFO] processing image 7985/9955
[INFO] processing image 7986/9955
[INFO] processing image 7987/9955
[INFO] processing image 7988/9955
[INFO] processing image 7989/9955
[INFO] processing image 7990/9955
[INFO] processing image 7991/9955
[INFO] processing image 7992/9955
[INFO] processing image 7993/9955
[INFO] processing image 7994/9955
[INFO] processing image 7995/9955
[INFO] processing image 7996/9955
[INFO] processing image 7997/9955
[INFO] processing image 7998/9955
[INFO] processing image 7999/9955
[INFO] processing image 8000/9955
[INFO] processing image 8001/9955
[INFO] processing image 8002/9955
[INFO] processing image 8003/9955
[INFO] processing image 8004/9955
[INFO] processing image 8005/9955
[INFO] processing image 8006/9955
[INFO] processing image 8007/9955
[INFO] processing image 8008/9955
[INFO] processing image 8009/9955
[INFO] processing image 8010/9955
[INFO] processing image 8011/9955
[INFO] processing image 8012/9955
[INFO] processing image 8013/9955
[INFO] processing image 8014/9955
[INFO] processing image 8015/9955
[INFO] processing image 8016/9955
[INFO] processing image 8017/9955
[INFO] processing image 8018/9955
[INFO] processing image 8019/9955
[INFO] processing image 8020/9955
[INFO] processing image 8021/9955
[INFO] processing image 8022/9955
[INFO] processing image 8023/9955
[INFO] processing image 8024/9955
[INFO] processing image 8025/9955
[INFO] processing image 8026/9955
[INFO] processing image 8027/9955
[INFO] processing image 8028/9955
[INFO] processing image 8029/9955
[INFO] processing image 8030/9955
[INFO] processing image 8031/9955
[INFO] processing image 8032/9955
[INFO] processing image 8033/9955
[INFO] processing image 8034/9955
[INFO] processing image 8035/9955
[INFO] processing image 8036/9955
[INFO] processing image 8037/9955
[INFO] processing image 8038/9955
[INFO] processing image 8039/9955
[INFO] processing image 8040/9955
[INFO] processing image 8041/9955
[INFO] processing image 8042/9955
[INFO] processing image 8043/9955
[INFO] processing image 8044/9955
[INFO] processing image 8045/9955
[INFO] processing image 8046/9955
[INFO] processing image 8047/9955
[INFO] processing image 8048/9955
[INFO] processing image 8049/9955
[INFO] processing image 8050/9955
[INFO] processing image 8051/9955
[INFO] processing image 8052/9955
[INFO] processing image 8053/9955
[INFO] processing image 8054/9955
[INFO] processing image 8055/9955
[INFO] processing image 8056/9955
[INFO] processing image 8057/9955
[INFO] processing image 8058/9955
[INFO] processing image 8059/9955
[INFO] processing image 8060/9955
[INFO] processing image 8061/9955
[INFO] processing image 8062/9955
[INFO] processing image 8063/9955
[INFO] processing image 8064/9955
[INFO] processing image 8065/9955
[INFO] processing image 8066/9955
[INFO] processing image 8067/9955
[INFO] processing image 8068/9955
[INFO] processing image 8069/9955
[INFO] processing image 8070/9955
[INFO] processing image 8071/9955
[INFO] processing image 8072/9955
[INFO] processing image 8073/9955
[INFO] processing image 8074/9955
[INFO] processing image 8075/9955
[INFO] processing image 8076/9955
[INFO] processing image 8077/9955
[INFO] processing image 8078/9955
[INFO] processing image 8079/9955
[INFO] processing image 8080/9955
[INFO] processing image 8081/9955
[INFO] processing image 8082/9955
[INFO] processing image 8083/9955
[INFO] processing image 8084/9955
[INFO] processing image 8085/9955
[INFO] processing image 8086/9955
[INFO] processing image 8087/9955
[INFO] processing image 8088/9955
[INFO] processing image 8089/9955
[INFO] processing image 8090/9955
[INFO] processing image 8091/9955
[INFO] processing image 8092/9955
[INFO] processing image 8093/9955
[INFO] processing image 8094/9955
[INFO] processing image 8095/9955
[INFO] processing image 8096/9955
[INFO] processing image 8097/9955
[INFO] processing image 8098/9955
[INFO] processing image 8099/9955
[INFO] processing image 8100/9955
[INFO] processing image 8101/9955
[INFO] processing image 8102/9955
[INFO] processing image 8103/9955
[INFO] processing image 8104/9955
[INFO] processing image 8105/9955
[INFO] processing image 8106/9955
[INFO] processing image 8107/9955
[INFO] processing image 8108/9955
[INFO] processing image 8109/9955
[INFO] processing image 8110/9955
[INFO] processing image 8111/9955
[INFO] processing image 8112/9955
[INFO] processing image 8113/9955
[INFO] processing image 8114/9955
[INFO] processing image 8115/9955
[INFO] processing image 8116/9955
[INFO] processing image 8117/9955
[INFO] processing image 8118/9955
[INFO] processing image 8119/9955
[INFO] processing image 8120/9955
[INFO] processing image 8121/9955
[INFO] processing image 8122/9955
[INFO] processing image 8123/9955
[INFO] processing image 8124/9955
[INFO] processing image 8125/9955
[INFO] processing image 8126/9955
[INFO] processing image 8127/9955
[INFO] processing image 8128/9955
[INFO] processing image 8129/9955
[INFO] processing image 8130/9955
[INFO] processing image 8131/9955
[INFO] processing image 8132/9955
[INFO] processing image 8133/9955
[INFO] processing image 8134/9955
[INFO] processing image 8135/9955
[INFO] processing image 8136/9955
[INFO] processing image 8137/9955
[INFO] processing image 8138/9955
[INFO] processing image 8139/9955
[INFO] processing image 8140/9955
[INFO] processing image 8141/9955
[INFO] processing image 8142/9955
[INFO] processing image 8143/9955
[INFO] processing image 8144/9955
[INFO] processing image 8145/9955
[INFO] processing image 8146/9955
[INFO] processing image 8147/9955
[INFO] processing image 8148/9955
[INFO] processing image 8149/9955
[INFO] processing image 8150/9955
[INFO] processing image 8151/9955
[INFO] processing image 8152/9955
[INFO] processing image 8153/9955
[INFO] processing image 8154/9955
[INFO] processing image 8155/9955
[INFO] processing image 8156/9955
[INFO] processing image 8157/9955
[INFO] processing image 8158/9955
[INFO] processing image 8159/9955
[INFO] processing image 8160/9955
[INFO] processing image 8161/9955
[INFO] processing image 8162/9955
[INFO] processing image 8163/9955
[INFO] processing image 8164/9955
[INFO] processing image 8165/9955
[INFO] processing image 8166/9955
[INFO] processing image 8167/9955
[INFO] processing image 8168/9955
[INFO] processing image 8169/9955
[INFO] processing image 8170/9955
[INFO] processing image 8171/9955
[INFO] processing image 8172/9955
[INFO] processing image 8173/9955
[INFO] processing image 8174/9955
[INFO] processing image 8175/9955
[INFO] processing image 8176/9955
[INFO] processing image 8177/9955
[INFO] processing image 8178/9955
[INFO] processing image 8179/9955
[INFO] processing image 8180/9955
[INFO] processing image 8181/9955
[INFO] processing image 8182/9955
[INFO] processing image 8183/9955
[INFO] processing image 8184/9955
[INFO] processing image 8185/9955
[INFO] processing image 8186/9955
[INFO] processing image 8187/9955
[INFO] processing image 8188/9955
[INFO] processing image 8189/9955
[INFO] processing image 8190/9955
[INFO] processing image 8191/9955
[INFO] processing image 8192/9955
[INFO] processing image 8193/9955
[INFO] processing image 8194/9955
[INFO] processing image 8195/9955
[INFO] processing image 8196/9955
[INFO] processing image 8197/9955
[INFO] processing image 8198/9955
[INFO] processing image 8199/9955
[INFO] processing image 8200/9955
[INFO] processing image 8201/9955
[INFO] processing image 8202/9955
[INFO] processing image 8203/9955
[INFO] processing image 8204/9955
[INFO] processing image 8205/9955
[INFO] processing image 8206/9955
[INFO] processing image 8207/9955
[INFO] processing image 8208/9955
[INFO] processing image 8209/9955
[INFO] processing image 8210/9955
[INFO] processing image 8211/9955
[INFO] processing image 8212/9955
[INFO] processing image 8213/9955
[INFO] processing image 8214/9955
[INFO] processing image 8215/9955
[INFO] processing image 8216/9955
[INFO] processing image 8217/9955
[INFO] processing image 8218/9955
[INFO] processing image 8219/9955
[INFO] processing image 8220/9955
[INFO] processing image 8221/9955
[INFO] processing image 8222/9955
[INFO] processing image 8223/9955
[INFO] processing image 8224/9955
[INFO] processing image 8225/9955
[INFO] processing image 8226/9955
[INFO] processing image 8227/9955
[INFO] processing image 8228/9955
[INFO] processing image 8229/9955
[INFO] processing image 8230/9955
[INFO] processing image 8231/9955
[INFO] processing image 8232/9955
[INFO] processing image 8233/9955
[INFO] processing image 8234/9955
[INFO] processing image 8235/9955
[INFO] processing image 8236/9955
[INFO] processing image 8237/9955
[INFO] processing image 8238/9955
[INFO] processing image 8239/9955
[INFO] processing image 8240/9955
[INFO] processing image 8241/9955
[INFO] processing image 8242/9955
[INFO] processing image 8243/9955
[INFO] processing image 8244/9955
[INFO] processing image 8245/9955
[INFO] processing image 8246/9955
[INFO] processing image 8247/9955
[INFO] processing image 8248/9955
[INFO] processing image 8249/9955
[INFO] processing image 8250/9955
[INFO] processing image 8251/9955
[INFO] processing image 8252/9955
[INFO] processing image 8253/9955
[INFO] processing image 8254/9955
[INFO] processing image 8255/9955
[INFO] processing image 8256/9955
[INFO] processing image 8257/9955
[INFO] processing image 8258/9955
[INFO] processing image 8259/9955
[INFO] processing image 8260/9955
[INFO] processing image 8261/9955
[INFO] processing image 8262/9955
[INFO] processing image 8263/9955
[INFO] processing image 8264/9955
[INFO] processing image 8265/9955
[INFO] processing image 8266/9955
[INFO] processing image 8267/9955
[INFO] processing image 8268/9955
[INFO] processing image 8269/9955
[INFO] processing image 8270/9955
[INFO] processing image 8271/9955
[INFO] processing image 8272/9955
[INFO] processing image 8273/9955
[INFO] processing image 8274/9955
[INFO] processing image 8275/9955
[INFO] processing image 8276/9955
[INFO] processing image 8277/9955
[INFO] processing image 8278/9955
[INFO] processing image 8279/9955
[INFO] processing image 8280/9955
[INFO] processing image 8281/9955
[INFO] processing image 8282/9955
[INFO] processing image 8283/9955
[INFO] processing image 8284/9955
[INFO] processing image 8285/9955
[INFO] processing image 8286/9955
[INFO] processing image 8287/9955
[INFO] processing image 8288/9955
[INFO] processing image 8289/9955
[INFO] processing image 8290/9955
[INFO] processing image 8291/9955
[INFO] processing image 8292/9955
[INFO] processing image 8293/9955
[INFO] processing image 8294/9955
[INFO] processing image 8295/9955
[INFO] processing image 8296/9955
[INFO] processing image 8297/9955
[INFO] processing image 8298/9955
[INFO] processing image 8299/9955
[INFO] processing image 8300/9955
[INFO] processing image 8301/9955
[INFO] processing image 8302/9955
[INFO] processing image 8303/9955
[INFO] processing image 8304/9955
[INFO] processing image 8305/9955
[INFO] processing image 8306/9955
[INFO] processing image 8307/9955
[INFO] processing image 8308/9955
[INFO] processing image 8309/9955
[INFO] processing image 8310/9955
[INFO] processing image 8311/9955
[INFO] processing image 8312/9955
[INFO] processing image 8313/9955
[INFO] processing image 8314/9955
[INFO] processing image 8315/9955
[INFO] processing image 8316/9955
[INFO] processing image 8317/9955
[INFO] processing image 8318/9955
[INFO] processing image 8319/9955
[INFO] processing image 8320/9955
[INFO] processing image 8321/9955
[INFO] processing image 8322/9955
[INFO] processing image 8323/9955
[INFO] processing image 8324/9955
[INFO] processing image 8325/9955
[INFO] processing image 8326/9955
[INFO] processing image 8327/9955
[INFO] processing image 8328/9955
[INFO] processing image 8329/9955
[INFO] processing image 8330/9955
[INFO] processing image 8331/9955
[INFO] processing image 8332/9955
[INFO] processing image 8333/9955
[INFO] processing image 8334/9955
[INFO] processing image 8335/9955
[INFO] processing image 8336/9955
[INFO] processing image 8337/9955
[INFO] processing image 8338/9955
[INFO] processing image 8339/9955
[INFO] processing image 8340/9955
[INFO] processing image 8341/9955
[INFO] processing image 8342/9955
[INFO] processing image 8343/9955
[INFO] processing image 8344/9955
[INFO] processing image 8345/9955
[INFO] processing image 8346/9955
[INFO] processing image 8347/9955
[INFO] processing image 8348/9955
[INFO] processing image 8349/9955
[INFO] processing image 8350/9955
[INFO] processing image 8351/9955
[INFO] processing image 8352/9955
[INFO] processing image 8353/9955
[INFO] processing image 8354/9955
[INFO] processing image 8355/9955
[INFO] processing image 8356/9955
[INFO] processing image 8357/9955
[INFO] processing image 8358/9955
[INFO] processing image 8359/9955
[INFO] processing image 8360/9955
[INFO] processing image 8361/9955
[INFO] processing image 8362/9955
[INFO] processing image 8363/9955
[INFO] processing image 8364/9955
[INFO] processing image 8365/9955
[INFO] processing image 8366/9955
[INFO] processing image 8367/9955
[INFO] processing image 8368/9955
[INFO] processing image 8369/9955
[INFO] processing image 8370/9955
[INFO] processing image 8371/9955
[INFO] processing image 8372/9955
[INFO] processing image 8373/9955
[INFO] processing image 8374/9955
[INFO] processing image 8375/9955
[INFO] processing image 8376/9955
[INFO] processing image 8377/9955
[INFO] processing image 8378/9955
[INFO] processing image 8379/9955
[INFO] processing image 8380/9955
[INFO] processing image 8381/9955
[INFO] processing image 8382/9955
[INFO] processing image 8383/9955
[INFO] processing image 8384/9955
[INFO] processing image 8385/9955
[INFO] processing image 8386/9955
[INFO] processing image 8387/9955
[INFO] processing image 8388/9955
[INFO] processing image 8389/9955
[INFO] processing image 8390/9955
[INFO] processing image 8391/9955
[INFO] processing image 8392/9955
[INFO] processing image 8393/9955
[INFO] processing image 8394/9955
[INFO] processing image 8395/9955
[INFO] processing image 8396/9955
[INFO] processing image 8397/9955
[INFO] processing image 8398/9955
[INFO] processing image 8399/9955
[INFO] processing image 8400/9955
[INFO] processing image 8401/9955
[INFO] processing image 8402/9955
[INFO] processing image 8403/9955
[INFO] processing image 8404/9955
[INFO] processing image 8405/9955
[INFO] processing image 8406/9955
[INFO] processing image 8407/9955
[INFO] processing image 8408/9955
[INFO] processing image 8409/9955
[INFO] processing image 8410/9955
[INFO] processing image 8411/9955
[INFO] processing image 8412/9955
[INFO] processing image 8413/9955
[INFO] processing image 8414/9955
[INFO] processing image 8415/9955
[INFO] processing image 8416/9955
[INFO] processing image 8417/9955
[INFO] processing image 8418/9955
[INFO] processing image 8419/9955
[INFO] processing image 8420/9955
[INFO] processing image 8421/9955
[INFO] processing image 8422/9955
[INFO] processing image 8423/9955
[INFO] processing image 8424/9955
[INFO] processing image 8425/9955
[INFO] processing image 8426/9955
[INFO] processing image 8427/9955
[INFO] processing image 8428/9955
[INFO] processing image 8429/9955
[INFO] processing image 8430/9955
[INFO] processing image 8431/9955
[INFO] processing image 8432/9955
[INFO] processing image 8433/9955
[INFO] processing image 8434/9955
[INFO] processing image 8435/9955
[INFO] processing image 8436/9955
[INFO] processing image 8437/9955
[INFO] processing image 8438/9955
[INFO] processing image 8439/9955
[INFO] processing image 8440/9955
[INFO] processing image 8441/9955
[INFO] processing image 8442/9955
[INFO] processing image 8443/9955
[INFO] processing image 8444/9955
[INFO] processing image 8445/9955
[INFO] processing image 8446/9955
[INFO] processing image 8447/9955
[INFO] processing image 8448/9955
[INFO] processing image 8449/9955
[INFO] processing image 8450/9955
[INFO] processing image 8451/9955
[INFO] processing image 8452/9955
[INFO] processing image 8453/9955
[INFO] processing image 8454/9955
[INFO] processing image 8455/9955
[INFO] processing image 8456/9955
[INFO] processing image 8457/9955
[INFO] processing image 8458/9955
[INFO] processing image 8459/9955
[INFO] processing image 8460/9955
[INFO] processing image 8461/9955
[INFO] processing image 8462/9955
[INFO] processing image 8463/9955
[INFO] processing image 8464/9955
[INFO] processing image 8465/9955
[INFO] processing image 8466/9955
[INFO] processing image 8467/9955
[INFO] processing image 8468/9955
[INFO] processing image 8469/9955
[INFO] processing image 8470/9955
[INFO] processing image 8471/9955
[INFO] processing image 8472/9955
[INFO] processing image 8473/9955
[INFO] processing image 8474/9955
[INFO] processing image 8475/9955
[INFO] processing image 8476/9955
[INFO] processing image 8477/9955
[INFO] processing image 8478/9955
[INFO] processing image 8479/9955
[INFO] processing image 8480/9955
[INFO] processing image 8481/9955
[INFO] processing image 8482/9955
[INFO] processing image 8483/9955
[INFO] processing image 8484/9955
[INFO] processing image 8485/9955
[INFO] processing image 8486/9955
[INFO] processing image 8487/9955
[INFO] processing image 8488/9955
[INFO] processing image 8489/9955
[INFO] processing image 8490/9955
[INFO] processing image 8491/9955
[INFO] processing image 8492/9955
[INFO] processing image 8493/9955
[INFO] processing image 8494/9955
[INFO] processing image 8495/9955
[INFO] processing image 8496/9955
[INFO] processing image 8497/9955
[INFO] processing image 8498/9955
[INFO] processing image 8499/9955
[INFO] processing image 8500/9955
[INFO] processing image 8501/9955
[INFO] processing image 8502/9955
[INFO] processing image 8503/9955
[INFO] processing image 8504/9955
[INFO] processing image 8505/9955
[INFO] processing image 8506/9955
[INFO] processing image 8507/9955
[INFO] processing image 8508/9955
[INFO] processing image 8509/9955
[INFO] processing image 8510/9955
[INFO] processing image 8511/9955
[INFO] processing image 8512/9955
[INFO] processing image 8513/9955
[INFO] processing image 8514/9955
[INFO] processing image 8515/9955
[INFO] processing image 8516/9955
[INFO] processing image 8517/9955
[INFO] processing image 8518/9955
[INFO] processing image 8519/9955
[INFO] processing image 8520/9955
[INFO] processing image 8521/9955
[INFO] processing image 8522/9955
[INFO] processing image 8523/9955
[INFO] processing image 8524/9955
[INFO] processing image 8525/9955
[INFO] processing image 8526/9955
[INFO] processing image 8527/9955
[INFO] processing image 8528/9955
[INFO] processing image 8529/9955
[INFO] processing image 8530/9955
[INFO] processing image 8531/9955
[INFO] processing image 8532/9955
[INFO] processing image 8533/9955
[INFO] processing image 8534/9955
[INFO] processing image 8535/9955
[INFO] processing image 8536/9955
[INFO] processing image 8537/9955
[INFO] processing image 8538/9955
[INFO] processing image 8539/9955
[INFO] processing image 8540/9955
[INFO] processing image 8541/9955
[INFO] processing image 8542/9955
[INFO] processing image 8543/9955
[INFO] processing image 8544/9955
[INFO] processing image 8545/9955
[INFO] processing image 8546/9955
[INFO] processing image 8547/9955
[INFO] processing image 8548/9955
[INFO] processing image 8549/9955
[INFO] processing image 8550/9955
[INFO] processing image 8551/9955
[INFO] processing image 8552/9955
[INFO] processing image 8553/9955
[INFO] processing image 8554/9955
[INFO] processing image 8555/9955
[INFO] processing image 8556/9955
[INFO] processing image 8557/9955
[INFO] processing image 8558/9955
[INFO] processing image 8559/9955
[INFO] processing image 8560/9955
[INFO] processing image 8561/9955
[INFO] processing image 8562/9955
[INFO] processing image 8563/9955
[INFO] processing image 8564/9955
[INFO] processing image 8565/9955
[INFO] processing image 8566/9955
[INFO] processing image 8567/9955
[INFO] processing image 8568/9955
[INFO] processing image 8569/9955
[INFO] processing image 8570/9955
[INFO] processing image 8571/9955
[INFO] processing image 8572/9955
[INFO] processing image 8573/9955
[INFO] processing image 8574/9955
[INFO] processing image 8575/9955
[INFO] processing image 8576/9955
[INFO] processing image 8577/9955
[INFO] processing image 8578/9955
[INFO] processing image 8579/9955
[INFO] processing image 8580/9955
[INFO] processing image 8581/9955
[INFO] processing image 8582/9955
[INFO] processing image 8583/9955
[INFO] processing image 8584/9955
[INFO] processing image 8585/9955
[INFO] processing image 8586/9955
[INFO] processing image 8587/9955
[INFO] processing image 8588/9955
[INFO] processing image 8589/9955
[INFO] processing image 8590/9955
[INFO] processing image 8591/9955
[INFO] processing image 8592/9955
[INFO] processing image 8593/9955
[INFO] processing image 8594/9955
[INFO] processing image 8595/9955
[INFO] processing image 8596/9955
[INFO] processing image 8597/9955
[INFO] processing image 8598/9955
[INFO] processing image 8599/9955
[INFO] processing image 8600/9955
[INFO] processing image 8601/9955
[INFO] processing image 8602/9955
[INFO] processing image 8603/9955
[INFO] processing image 8604/9955
[INFO] processing image 8605/9955
[INFO] processing image 8606/9955
[INFO] processing image 8607/9955
[INFO] processing image 8608/9955
[INFO] processing image 8609/9955
[INFO] processing image 8610/9955
[INFO] processing image 8611/9955
[INFO] processing image 8612/9955
[INFO] processing image 8613/9955
[INFO] processing image 8614/9955
[INFO] processing image 8615/9955
[INFO] processing image 8616/9955
[INFO] processing image 8617/9955
[INFO] processing image 8618/9955
[INFO] processing image 8619/9955
[INFO] processing image 8620/9955
[INFO] processing image 8621/9955
[INFO] processing image 8622/9955
[INFO] processing image 8623/9955
[INFO] processing image 8624/9955
[INFO] processing image 8625/9955
[INFO] processing image 8626/9955
[INFO] processing image 8627/9955
[INFO] processing image 8628/9955
[INFO] processing image 8629/9955
[INFO] processing image 8630/9955
[INFO] processing image 8631/9955
[INFO] processing image 8632/9955
[INFO] processing image 8633/9955
[INFO] processing image 8634/9955
[INFO] processing image 8635/9955
[INFO] processing image 8636/9955
[INFO] processing image 8637/9955
[INFO] processing image 8638/9955
[INFO] processing image 8639/9955
[INFO] processing image 8640/9955
[INFO] processing image 8641/9955
[INFO] processing image 8642/9955
[INFO] processing image 8643/9955
[INFO] processing image 8644/9955
[INFO] processing image 8645/9955
[INFO] processing image 8646/9955
[INFO] processing image 8647/9955
[INFO] processing image 8648/9955
[INFO] processing image 8649/9955
[INFO] processing image 8650/9955
[INFO] processing image 8651/9955
[INFO] processing image 8652/9955
[INFO] processing image 8653/9955
[INFO] processing image 8654/9955
[INFO] processing image 8655/9955
[INFO] processing image 8656/9955
[INFO] processing image 8657/9955
[INFO] processing image 8658/9955
[INFO] processing image 8659/9955
[INFO] processing image 8660/9955
[INFO] processing image 8661/9955
[INFO] processing image 8662/9955
[INFO] processing image 8663/9955
[INFO] processing image 8664/9955
[INFO] processing image 8665/9955
[INFO] processing image 8666/9955
[INFO] processing image 8667/9955
[INFO] processing image 8668/9955
[INFO] processing image 8669/9955
[INFO] processing image 8670/9955
[INFO] processing image 8671/9955
[INFO] processing image 8672/9955
[INFO] processing image 8673/9955
[INFO] processing image 8674/9955
[INFO] processing image 8675/9955
[INFO] processing image 8676/9955
[INFO] processing image 8677/9955
[INFO] processing image 8678/9955
[INFO] processing image 8679/9955
[INFO] processing image 8680/9955
[INFO] processing image 8681/9955
[INFO] processing image 8682/9955
[INFO] processing image 8683/9955
[INFO] processing image 8684/9955
[INFO] processing image 8685/9955
[INFO] processing image 8686/9955
[INFO] processing image 8687/9955
[INFO] processing image 8688/9955
[INFO] processing image 8689/9955
[INFO] processing image 8690/9955
[INFO] processing image 8691/9955
[INFO] processing image 8692/9955
[INFO] processing image 8693/9955
[INFO] processing image 8694/9955
[INFO] processing image 8695/9955
[INFO] processing image 8696/9955
[INFO] processing image 8697/9955
[INFO] processing image 8698/9955
[INFO] processing image 8699/9955
[INFO] processing image 8700/9955
[INFO] processing image 8701/9955
[INFO] processing image 8702/9955
[INFO] processing image 8703/9955
[INFO] processing image 8704/9955
[INFO] processing image 8705/9955
[INFO] processing image 8706/9955
[INFO] processing image 8707/9955
[INFO] processing image 8708/9955
[INFO] processing image 8709/9955
[INFO] processing image 8710/9955
[INFO] processing image 8711/9955
[INFO] processing image 8712/9955
[INFO] processing image 8713/9955
[INFO] processing image 8714/9955
[INFO] processing image 8715/9955
[INFO] processing image 8716/9955
[INFO] processing image 8717/9955
[INFO] processing image 8718/9955
[INFO] processing image 8719/9955
[INFO] processing image 8720/9955
[INFO] processing image 8721/9955
[INFO] processing image 8722/9955
[INFO] processing image 8723/9955
[INFO] processing image 8724/9955
[INFO] processing image 8725/9955
[INFO] processing image 8726/9955
[INFO] processing image 8727/9955
[INFO] processing image 8728/9955
[INFO] processing image 8729/9955
[INFO] processing image 8730/9955
[INFO] processing image 8731/9955
[INFO] processing image 8732/9955
[INFO] processing image 8733/9955
[INFO] processing image 8734/9955
[INFO] processing image 8735/9955
[INFO] processing image 8736/9955
[INFO] processing image 8737/9955
[INFO] processing image 8738/9955
[INFO] processing image 8739/9955
[INFO] processing image 8740/9955
[INFO] processing image 8741/9955
[INFO] processing image 8742/9955
[INFO] processing image 8743/9955
[INFO] processing image 8744/9955
[INFO] processing image 8745/9955
[INFO] processing image 8746/9955
[INFO] processing image 8747/9955
[INFO] processing image 8748/9955
[INFO] processing image 8749/9955
[INFO] processing image 8750/9955
[INFO] processing image 8751/9955
[INFO] processing image 8752/9955
[INFO] processing image 8753/9955
[INFO] processing image 8754/9955
[INFO] processing image 8755/9955
[INFO] processing image 8756/9955
[INFO] processing image 8757/9955
[INFO] processing image 8758/9955
[INFO] processing image 8759/9955
[INFO] processing image 8760/9955
[INFO] processing image 8761/9955
[INFO] processing image 8762/9955
[INFO] processing image 8763/9955
[INFO] processing image 8764/9955
[INFO] processing image 8765/9955
[INFO] processing image 8766/9955
[INFO] processing image 8767/9955
[INFO] processing image 8768/9955
[INFO] processing image 8769/9955
[INFO] processing image 8770/9955
[INFO] processing image 8771/9955
[INFO] processing image 8772/9955
[INFO] processing image 8773/9955
[INFO] processing image 8774/9955
[INFO] processing image 8775/9955
[INFO] processing image 8776/9955
[INFO] processing image 8777/9955
[INFO] processing image 8778/9955
[INFO] processing image 8779/9955
[INFO] processing image 8780/9955
[INFO] processing image 8781/9955
[INFO] processing image 8782/9955
[INFO] processing image 8783/9955
[INFO] processing image 8784/9955
[INFO] processing image 8785/9955
[INFO] processing image 8786/9955
[INFO] processing image 8787/9955
[INFO] processing image 8788/9955
[INFO] processing image 8789/9955
[INFO] processing image 8790/9955
[INFO] processing image 8791/9955
[INFO] processing image 8792/9955
[INFO] processing image 8793/9955
[INFO] processing image 8794/9955
[INFO] processing image 8795/9955
[INFO] processing image 8796/9955
[INFO] processing image 8797/9955
[INFO] processing image 8798/9955
[INFO] processing image 8799/9955
[INFO] processing image 8800/9955
[INFO] processing image 8801/9955
[INFO] processing image 8802/9955
[INFO] processing image 8803/9955
[INFO] processing image 8804/9955
[INFO] processing image 8805/9955
[INFO] processing image 8806/9955
[INFO] processing image 8807/9955
[INFO] processing image 8808/9955
[INFO] processing image 8809/9955
[INFO] processing image 8810/9955
[INFO] processing image 8811/9955
[INFO] processing image 8812/9955
[INFO] processing image 8813/9955
[INFO] processing image 8814/9955
[INFO] processing image 8815/9955
[INFO] processing image 8816/9955
[INFO] processing image 8817/9955
[INFO] processing image 8818/9955
[INFO] processing image 8819/9955
[INFO] processing image 8820/9955
[INFO] processing image 8821/9955
[INFO] processing image 8822/9955
[INFO] processing image 8823/9955
[INFO] processing image 8824/9955
[INFO] processing image 8825/9955
[INFO] processing image 8826/9955
[INFO] processing image 8827/9955
[INFO] processing image 8828/9955
[INFO] processing image 8829/9955
[INFO] processing image 8830/9955
[INFO] processing image 8831/9955
[INFO] processing image 8832/9955
[INFO] processing image 8833/9955
[INFO] processing image 8834/9955
[INFO] processing image 8835/9955
[INFO] processing image 8836/9955
[INFO] processing image 8837/9955
[INFO] processing image 8838/9955
[INFO] processing image 8839/9955
[INFO] processing image 8840/9955
[INFO] processing image 8841/9955
[INFO] processing image 8842/9955
[INFO] processing image 8843/9955
[INFO] processing image 8844/9955
[INFO] processing image 8845/9955
[INFO] processing image 8846/9955
[INFO] processing image 8847/9955
[INFO] processing image 8848/9955
[INFO] processing image 8849/9955
[INFO] processing image 8850/9955
[INFO] processing image 8851/9955
[INFO] processing image 8852/9955
[INFO] processing image 8853/9955
[INFO] processing image 8854/9955
[INFO] processing image 8855/9955
[INFO] processing image 8856/9955
[INFO] processing image 8857/9955
[INFO] processing image 8858/9955
[INFO] processing image 8859/9955
[INFO] processing image 8860/9955
[INFO] processing image 8861/9955
[INFO] processing image 8862/9955
[INFO] processing image 8863/9955
[INFO] processing image 8864/9955
[INFO] processing image 8865/9955
[INFO] processing image 8866/9955
[INFO] processing image 8867/9955
[INFO] processing image 8868/9955
[INFO] processing image 8869/9955
[INFO] processing image 8870/9955
[INFO] processing image 8871/9955
[INFO] processing image 8872/9955
[INFO] processing image 8873/9955
[INFO] processing image 8874/9955
[INFO] processing image 8875/9955
[INFO] processing image 8876/9955
[INFO] processing image 8877/9955
[INFO] processing image 8878/9955
[INFO] processing image 8879/9955
[INFO] processing image 8880/9955
[INFO] processing image 8881/9955
[INFO] processing image 8882/9955
[INFO] processing image 8883/9955
[INFO] processing image 8884/9955
[INFO] processing image 8885/9955
[INFO] processing image 8886/9955
[INFO] processing image 8887/9955
[INFO] processing image 8888/9955
[INFO] processing image 8889/9955
[INFO] processing image 8890/9955
[INFO] processing image 8891/9955
[INFO] processing image 8892/9955
[INFO] processing image 8893/9955
[INFO] processing image 8894/9955
[INFO] processing image 8895/9955
[INFO] processing image 8896/9955
[INFO] processing image 8897/9955
[INFO] processing image 8898/9955
[INFO] processing image 8899/9955
[INFO] processing image 8900/9955
[INFO] processing image 8901/9955
[INFO] processing image 8902/9955
[INFO] processing image 8903/9955
[INFO] processing image 8904/9955
[INFO] processing image 8905/9955
[INFO] processing image 8906/9955
[INFO] processing image 8907/9955
[INFO] processing image 8908/9955
[INFO] processing image 8909/9955
[INFO] processing image 8910/9955
[INFO] processing image 8911/9955
[INFO] processing image 8912/9955
[INFO] processing image 8913/9955
[INFO] processing image 8914/9955
[INFO] processing image 8915/9955
[INFO] processing image 8916/9955
[INFO] processing image 8917/9955
[INFO] processing image 8918/9955
[INFO] processing image 8919/9955
[INFO] processing image 8920/9955
[INFO] processing image 8921/9955
[INFO] processing image 8922/9955
[INFO] processing image 8923/9955
[INFO] processing image 8924/9955
[INFO] processing image 8925/9955
[INFO] processing image 8926/9955
[INFO] processing image 8927/9955
[INFO] processing image 8928/9955
[INFO] processing image 8929/9955
[INFO] processing image 8930/9955
[INFO] processing image 8931/9955
[INFO] processing image 8932/9955
[INFO] processing image 8933/9955
[INFO] processing image 8934/9955
[INFO] processing image 8935/9955
[INFO] processing image 8936/9955
[INFO] processing image 8937/9955
[INFO] processing image 8938/9955
[INFO] processing image 8939/9955
[INFO] processing image 8940/9955
[INFO] processing image 8941/9955
[INFO] processing image 8942/9955
[INFO] processing image 8943/9955
[INFO] processing image 8944/9955
[INFO] processing image 8945/9955
[INFO] processing image 8946/9955
[INFO] processing image 8947/9955
[INFO] processing image 8948/9955
[INFO] processing image 8949/9955
[INFO] processing image 8950/9955
[INFO] processing image 8951/9955
[INFO] processing image 8952/9955
[INFO] processing image 8953/9955
[INFO] processing image 8954/9955
[INFO] processing image 8955/9955
[INFO] processing image 8956/9955
[INFO] processing image 8957/9955
[INFO] processing image 8958/9955
[INFO] processing image 8959/9955
[INFO] processing image 8960/9955
[INFO] processing image 8961/9955
[INFO] processing image 8962/9955
[INFO] processing image 8963/9955
[INFO] processing image 8964/9955
[INFO] processing image 8965/9955
[INFO] processing image 8966/9955
[INFO] processing image 8967/9955
[INFO] processing image 8968/9955
[INFO] processing image 8969/9955
[INFO] processing image 8970/9955
[INFO] processing image 8971/9955
[INFO] processing image 8972/9955
[INFO] processing image 8973/9955
[INFO] processing image 8974/9955
[INFO] processing image 8975/9955
[INFO] processing image 8976/9955
[INFO] processing image 8977/9955
[INFO] processing image 8978/9955
[INFO] processing image 8979/9955
[INFO] processing image 8980/9955
[INFO] processing image 8981/9955
[INFO] processing image 8982/9955
[INFO] processing image 8983/9955
[INFO] processing image 8984/9955
[INFO] processing image 8985/9955
[INFO] processing image 8986/9955
[INFO] processing image 8987/9955
[INFO] processing image 8988/9955
[INFO] processing image 8989/9955
[INFO] processing image 8990/9955
[INFO] processing image 8991/9955
[INFO] processing image 8992/9955
[INFO] processing image 8993/9955
[INFO] processing image 8994/9955
[INFO] processing image 8995/9955
[INFO] processing image 8996/9955
[INFO] processing image 8997/9955
[INFO] processing image 8998/9955
[INFO] processing image 8999/9955
[INFO] processing image 9000/9955
[INFO] processing image 9001/9955
[INFO] processing image 9002/9955
[INFO] processing image 9003/9955
[INFO] processing image 9004/9955
[INFO] processing image 9005/9955
[INFO] processing image 9006/9955
[INFO] processing image 9007/9955
[INFO] processing image 9008/9955
[INFO] processing image 9009/9955
[INFO] processing image 9010/9955
[INFO] processing image 9011/9955
[INFO] processing image 9012/9955
[INFO] processing image 9013/9955
[INFO] processing image 9014/9955
[INFO] processing image 9015/9955
[INFO] processing image 9016/9955
[INFO] processing image 9017/9955
[INFO] processing image 9018/9955
[INFO] processing image 9019/9955
[INFO] processing image 9020/9955
[INFO] processing image 9021/9955
[INFO] processing image 9022/9955
[INFO] processing image 9023/9955
[INFO] processing image 9024/9955
[INFO] processing image 9025/9955
[INFO] processing image 9026/9955
[INFO] processing image 9027/9955
[INFO] processing image 9028/9955
[INFO] processing image 9029/9955
[INFO] processing image 9030/9955
[INFO] processing image 9031/9955
[INFO] processing image 9032/9955
[INFO] processing image 9033/9955
[INFO] processing image 9034/9955
[INFO] processing image 9035/9955
[INFO] processing image 9036/9955
[INFO] processing image 9037/9955
[INFO] processing image 9038/9955
[INFO] processing image 9039/9955
[INFO] processing image 9040/9955
[INFO] processing image 9041/9955
[INFO] processing image 9042/9955
[INFO] processing image 9043/9955
[INFO] processing image 9044/9955
[INFO] processing image 9045/9955
[INFO] processing image 9046/9955
[INFO] processing image 9047/9955
[INFO] processing image 9048/9955
[INFO] processing image 9049/9955
[INFO] processing image 9050/9955
[INFO] processing image 9051/9955
[INFO] processing image 9052/9955
[INFO] processing image 9053/9955
[INFO] processing image 9054/9955
[INFO] processing image 9055/9955
[INFO] processing image 9056/9955
[INFO] processing image 9057/9955
[INFO] processing image 9058/9955
[INFO] processing image 9059/9955
[INFO] processing image 9060/9955
[INFO] processing image 9061/9955
[INFO] processing image 9062/9955
[INFO] processing image 9063/9955
[INFO] processing image 9064/9955
[INFO] processing image 9065/9955
[INFO] processing image 9066/9955
[INFO] processing image 9067/9955
[INFO] processing image 9068/9955
[INFO] processing image 9069/9955
[INFO] processing image 9070/9955
[INFO] processing image 9071/9955
[INFO] processing image 9072/9955
[INFO] processing image 9073/9955
[INFO] processing image 9074/9955
[INFO] processing image 9075/9955
[INFO] processing image 9076/9955
[INFO] processing image 9077/9955
[INFO] processing image 9078/9955
[INFO] processing image 9079/9955
[INFO] processing image 9080/9955
[INFO] processing image 9081/9955
[INFO] processing image 9082/9955
[INFO] processing image 9083/9955
[INFO] processing image 9084/9955
[INFO] processing image 9085/9955
[INFO] processing image 9086/9955
[INFO] processing image 9087/9955
[INFO] processing image 9088/9955
[INFO] processing image 9089/9955
[INFO] processing image 9090/9955
[INFO] processing image 9091/9955
[INFO] processing image 9092/9955
[INFO] processing image 9093/9955
[INFO] processing image 9094/9955
[INFO] processing image 9095/9955
[INFO] processing image 9096/9955
[INFO] processing image 9097/9955
[INFO] processing image 9098/9955
[INFO] processing image 9099/9955
[INFO] processing image 9100/9955
[INFO] processing image 9101/9955
[INFO] processing image 9102/9955
[INFO] processing image 9103/9955
[INFO] processing image 9104/9955
[INFO] processing image 9105/9955
[INFO] processing image 9106/9955
[INFO] processing image 9107/9955
[INFO] processing image 9108/9955
[INFO] processing image 9109/9955
[INFO] processing image 9110/9955
[INFO] processing image 9111/9955
[INFO] processing image 9112/9955
[INFO] processing image 9113/9955
[INFO] processing image 9114/9955
[INFO] processing image 9115/9955
[INFO] processing image 9116/9955
[INFO] processing image 9117/9955
[INFO] processing image 9118/9955
[INFO] processing image 9119/9955
[INFO] processing image 9120/9955
[INFO] processing image 9121/9955
[INFO] processing image 9122/9955
[INFO] processing image 9123/9955
[INFO] processing image 9124/9955
[INFO] processing image 9125/9955
[INFO] processing image 9126/9955
[INFO] processing image 9127/9955
[INFO] processing image 9128/9955
[INFO] processing image 9129/9955
[INFO] processing image 9130/9955
[INFO] processing image 9131/9955
[INFO] processing image 9132/9955
[INFO] processing image 9133/9955
[INFO] processing image 9134/9955
[INFO] processing image 9135/9955
[INFO] processing image 9136/9955
[INFO] processing image 9137/9955
[INFO] processing image 9138/9955
[INFO] processing image 9139/9955
[INFO] processing image 9140/9955
[INFO] processing image 9141/9955
[INFO] processing image 9142/9955
[INFO] processing image 9143/9955
[INFO] processing image 9144/9955
[INFO] processing image 9145/9955
[INFO] processing image 9146/9955
[INFO] processing image 9147/9955
[INFO] processing image 9148/9955
[INFO] processing image 9149/9955
[INFO] processing image 9150/9955
[INFO] processing image 9151/9955
[INFO] processing image 9152/9955
[INFO] processing image 9153/9955
[INFO] processing image 9154/9955
[INFO] processing image 9155/9955
[INFO] processing image 9156/9955
[INFO] processing image 9157/9955
[INFO] processing image 9158/9955
[INFO] processing image 9159/9955
[INFO] processing image 9160/9955
[INFO] processing image 9161/9955
[INFO] processing image 9162/9955
[INFO] processing image 9163/9955
[INFO] processing image 9164/9955
[INFO] processing image 9165/9955
[INFO] processing image 9166/9955
[INFO] processing image 9167/9955
[INFO] processing image 9168/9955
[INFO] processing image 9169/9955
[INFO] processing image 9170/9955
[INFO] processing image 9171/9955
[INFO] processing image 9172/9955
[INFO] processing image 9173/9955
[INFO] processing image 9174/9955
[INFO] processing image 9175/9955
[INFO] processing image 9176/9955
[INFO] processing image 9177/9955
[INFO] processing image 9178/9955
[INFO] processing image 9179/9955
[INFO] processing image 9180/9955
[INFO] processing image 9181/9955
[INFO] processing image 9182/9955
[INFO] processing image 9183/9955
[INFO] processing image 9184/9955
[INFO] processing image 9185/9955
[INFO] processing image 9186/9955
[INFO] processing image 9187/9955
[INFO] processing image 9188/9955
[INFO] processing image 9189/9955
[INFO] processing image 9190/9955
[INFO] processing image 9191/9955
[INFO] processing image 9192/9955
[INFO] processing image 9193/9955
[INFO] processing image 9194/9955
[INFO] processing image 9195/9955
[INFO] processing image 9196/9955
[INFO] processing image 9197/9955
[INFO] processing image 9198/9955
[INFO] processing image 9199/9955
[INFO] processing image 9200/9955
[INFO] processing image 9201/9955
[INFO] processing image 9202/9955
[INFO] processing image 9203/9955
[INFO] processing image 9204/9955
[INFO] processing image 9205/9955
[INFO] processing image 9206/9955
[INFO] processing image 9207/9955
[INFO] processing image 9208/9955
[INFO] processing image 9209/9955
[INFO] processing image 9210/9955
[INFO] processing image 9211/9955
[INFO] processing image 9212/9955
[INFO] processing image 9213/9955
[INFO] processing image 9214/9955
[INFO] processing image 9215/9955
[INFO] processing image 9216/9955
[INFO] processing image 9217/9955
[INFO] processing image 9218/9955
[INFO] processing image 9219/9955
[INFO] processing image 9220/9955
[INFO] processing image 9221/9955
[INFO] processing image 9222/9955
[INFO] processing image 9223/9955
[INFO] processing image 9224/9955
[INFO] processing image 9225/9955
[INFO] processing image 9226/9955
[INFO] processing image 9227/9955
[INFO] processing image 9228/9955
[INFO] processing image 9229/9955
[INFO] processing image 9230/9955
[INFO] processing image 9231/9955
[INFO] processing image 9232/9955
[INFO] processing image 9233/9955
[INFO] processing image 9234/9955
[INFO] processing image 9235/9955
[INFO] processing image 9236/9955
[INFO] processing image 9237/9955
[INFO] processing image 9238/9955
[INFO] processing image 9239/9955
[INFO] processing image 9240/9955
[INFO] processing image 9241/9955
[INFO] processing image 9242/9955
[INFO] processing image 9243/9955
[INFO] processing image 9244/9955
[INFO] processing image 9245/9955
[INFO] processing image 9246/9955
[INFO] processing image 9247/9955
[INFO] processing image 9248/9955
[INFO] processing image 9249/9955
[INFO] processing image 9250/9955
[INFO] processing image 9251/9955
[INFO] processing image 9252/9955
[INFO] processing image 9253/9955
[INFO] processing image 9254/9955
[INFO] processing image 9255/9955
[INFO] processing image 9256/9955
[INFO] processing image 9257/9955
[INFO] processing image 9258/9955
[INFO] processing image 9259/9955
[INFO] processing image 9260/9955
[INFO] processing image 9261/9955
[INFO] processing image 9262/9955
[INFO] processing image 9263/9955
[INFO] processing image 9264/9955
[INFO] processing image 9265/9955
[INFO] processing image 9266/9955
[INFO] processing image 9267/9955
[INFO] processing image 9268/9955
[INFO] processing image 9269/9955
[INFO] processing image 9270/9955
[INFO] processing image 9271/9955
[INFO] processing image 9272/9955
[INFO] processing image 9273/9955
[INFO] processing image 9274/9955
[INFO] processing image 9275/9955
[INFO] processing image 9276/9955
[INFO] processing image 9277/9955
[INFO] processing image 9278/9955
[INFO] processing image 9279/9955
[INFO] processing image 9280/9955
[INFO] processing image 9281/9955
[INFO] processing image 9282/9955
[INFO] processing image 9283/9955
[INFO] processing image 9284/9955
[INFO] processing image 9285/9955
[INFO] processing image 9286/9955
[INFO] processing image 9287/9955
[INFO] processing image 9288/9955
[INFO] processing image 9289/9955
[INFO] processing image 9290/9955
[INFO] processing image 9291/9955
[INFO] processing image 9292/9955
[INFO] processing image 9293/9955
[INFO] processing image 9294/9955
[INFO] processing image 9295/9955
[INFO] processing image 9296/9955
[INFO] processing image 9297/9955
[INFO] processing image 9298/9955
[INFO] processing image 9299/9955
[INFO] processing image 9300/9955
[INFO] processing image 9301/9955
[INFO] processing image 9302/9955
[INFO] processing image 9303/9955
[INFO] processing image 9304/9955
[INFO] processing image 9305/9955
[INFO] processing image 9306/9955
[INFO] processing image 9307/9955
[INFO] processing image 9308/9955
[INFO] processing image 9309/9955
[INFO] processing image 9310/9955
[INFO] processing image 9311/9955
[INFO] processing image 9312/9955
[INFO] processing image 9313/9955
[INFO] processing image 9314/9955
[INFO] processing image 9315/9955
[INFO] processing image 9316/9955
[INFO] processing image 9317/9955
[INFO] processing image 9318/9955
[INFO] processing image 9319/9955
[INFO] processing image 9320/9955
[INFO] processing image 9321/9955
[INFO] processing image 9322/9955
[INFO] processing image 9323/9955
[INFO] processing image 9324/9955
[INFO] processing image 9325/9955
[INFO] processing image 9326/9955
[INFO] processing image 9327/9955
[INFO] processing image 9328/9955
[INFO] processing image 9329/9955
[INFO] processing image 9330/9955
[INFO] processing image 9331/9955
[INFO] processing image 9332/9955
[INFO] processing image 9333/9955
[INFO] processing image 9334/9955
[INFO] processing image 9335/9955
[INFO] processing image 9336/9955
[INFO] processing image 9337/9955
[INFO] processing image 9338/9955
[INFO] processing image 9339/9955
[INFO] processing image 9340/9955
[INFO] processing image 9341/9955
[INFO] processing image 9342/9955
[INFO] processing image 9343/9955
[INFO] processing image 9344/9955
[INFO] processing image 9345/9955
[INFO] processing image 9346/9955
[INFO] processing image 9347/9955
[INFO] processing image 9348/9955
[INFO] processing image 9349/9955
[INFO] processing image 9350/9955
[INFO] processing image 9351/9955
[INFO] processing image 9352/9955
[INFO] processing image 9353/9955
[INFO] processing image 9354/9955
[INFO] processing image 9355/9955
[INFO] processing image 9356/9955
[INFO] processing image 9357/9955
[INFO] processing image 9358/9955
[INFO] processing image 9359/9955
[INFO] processing image 9360/9955
[INFO] processing image 9361/9955
[INFO] processing image 9362/9955
[INFO] processing image 9363/9955
[INFO] processing image 9364/9955
[INFO] processing image 9365/9955
[INFO] processing image 9366/9955
[INFO] processing image 9367/9955
[INFO] processing image 9368/9955
[INFO] processing image 9369/9955
[INFO] processing image 9370/9955
[INFO] processing image 9371/9955
[INFO] processing image 9372/9955
[INFO] processing image 9373/9955
[INFO] processing image 9374/9955
[INFO] processing image 9375/9955
[INFO] processing image 9376/9955
[INFO] processing image 9377/9955
[INFO] processing image 9378/9955
[INFO] processing image 9379/9955
[INFO] processing image 9380/9955
[INFO] processing image 9381/9955
[INFO] processing image 9382/9955
[INFO] processing image 9383/9955
[INFO] processing image 9384/9955
[INFO] processing image 9385/9955
[INFO] processing image 9386/9955
[INFO] processing image 9387/9955
[INFO] processing image 9388/9955
[INFO] processing image 9389/9955
[INFO] processing image 9390/9955
[INFO] processing image 9391/9955
[INFO] processing image 9392/9955
[INFO] processing image 9393/9955
[INFO] processing image 9394/9955
[INFO] processing image 9395/9955
[INFO] processing image 9396/9955
[INFO] processing image 9397/9955
[INFO] processing image 9398/9955
[INFO] processing image 9399/9955
[INFO] processing image 9400/9955
[INFO] processing image 9401/9955
[INFO] processing image 9402/9955
[INFO] processing image 9403/9955
[INFO] processing image 9404/9955
[INFO] processing image 9405/9955
[INFO] processing image 9406/9955
[INFO] processing image 9407/9955
[INFO] processing image 9408/9955
[INFO] processing image 9409/9955
[INFO] processing image 9410/9955
[INFO] processing image 9411/9955
[INFO] processing image 9412/9955
[INFO] processing image 9413/9955
[INFO] processing image 9414/9955
[INFO] processing image 9415/9955
[INFO] processing image 9416/9955
[INFO] processing image 9417/9955
[INFO] processing image 9418/9955
[INFO] processing image 9419/9955
[INFO] processing image 9420/9955
[INFO] processing image 9421/9955
[INFO] processing image 9422/9955
[INFO] processing image 9423/9955
[INFO] processing image 9424/9955
[INFO] processing image 9425/9955
[INFO] processing image 9426/9955
[INFO] processing image 9427/9955
[INFO] processing image 9428/9955
[INFO] processing image 9429/9955
[INFO] processing image 9430/9955
[INFO] processing image 9431/9955
[INFO] processing image 9432/9955
[INFO] processing image 9433/9955
[INFO] processing image 9434/9955
[INFO] processing image 9435/9955
[INFO] processing image 9436/9955
[INFO] processing image 9437/9955
[INFO] processing image 9438/9955
[INFO] processing image 9439/9955
[INFO] processing image 9440/9955
[INFO] processing image 9441/9955
[INFO] processing image 9442/9955
[INFO] processing image 9443/9955
[INFO] processing image 9444/9955
[INFO] processing image 9445/9955
[INFO] processing image 9446/9955
[INFO] processing image 9447/9955
[INFO] processing image 9448/9955
[INFO] processing image 9449/9955
[INFO] processing image 9450/9955
[INFO] processing image 9451/9955
[INFO] processing image 9452/9955
[INFO] processing image 9453/9955
[INFO] processing image 9454/9955
[INFO] processing image 9455/9955
[INFO] processing image 9456/9955
[INFO] processing image 9457/9955
[INFO] processing image 9458/9955
[INFO] processing image 9459/9955
[INFO] processing image 9460/9955
[INFO] processing image 9461/9955
[INFO] processing image 9462/9955
[INFO] processing image 9463/9955
[INFO] processing image 9464/9955
[INFO] processing image 9465/9955
[INFO] processing image 9466/9955
[INFO] processing image 9467/9955
[INFO] processing image 9468/9955
[INFO] processing image 9469/9955
[INFO] processing image 9470/9955
[INFO] processing image 9471/9955
[INFO] processing image 9472/9955
[INFO] processing image 9473/9955
[INFO] processing image 9474/9955
[INFO] processing image 9475/9955
[INFO] processing image 9476/9955
[INFO] processing image 9477/9955
[INFO] processing image 9478/9955
[INFO] processing image 9479/9955
[INFO] processing image 9480/9955
[INFO] processing image 9481/9955
[INFO] processing image 9482/9955
[INFO] processing image 9483/9955
[INFO] processing image 9484/9955
[INFO] processing image 9485/9955
[INFO] processing image 9486/9955
[INFO] processing image 9487/9955
[INFO] processing image 9488/9955
[INFO] processing image 9489/9955
[INFO] processing image 9490/9955
[INFO] processing image 9491/9955
[INFO] processing image 9492/9955
[INFO] processing image 9493/9955
[INFO] processing image 9494/9955
[INFO] processing image 9495/9955
[INFO] processing image 9496/9955
[INFO] processing image 9497/9955
[INFO] processing image 9498/9955
[INFO] processing image 9499/9955
[INFO] processing image 9500/9955
[INFO] processing image 9501/9955
[INFO] processing image 9502/9955
[INFO] processing image 9503/9955
[INFO] processing image 9504/9955
[INFO] processing image 9505/9955
[INFO] processing image 9506/9955
[INFO] processing image 9507/9955
[INFO] processing image 9508/9955
[INFO] processing image 9509/9955
[INFO] processing image 9510/9955
[INFO] processing image 9511/9955
[INFO] processing image 9512/9955
[INFO] processing image 9513/9955
[INFO] processing image 9514/9955
[INFO] processing image 9515/9955
[INFO] processing image 9516/9955
[INFO] processing image 9517/9955
[INFO] processing image 9518/9955
[INFO] processing image 9519/9955
[INFO] processing image 9520/9955
[INFO] processing image 9521/9955
[INFO] processing image 9522/9955
[INFO] processing image 9523/9955
[INFO] processing image 9524/9955
[INFO] processing image 9525/9955
[INFO] processing image 9526/9955
[INFO] processing image 9527/9955
[INFO] processing image 9528/9955
[INFO] processing image 9529/9955
[INFO] processing image 9530/9955
[INFO] processing image 9531/9955
[INFO] processing image 9532/9955
[INFO] processing image 9533/9955
[INFO] processing image 9534/9955
[INFO] processing image 9535/9955
[INFO] processing image 9536/9955
[INFO] processing image 9537/9955
[INFO] processing image 9538/9955
[INFO] processing image 9539/9955
[INFO] processing image 9540/9955
[INFO] processing image 9541/9955
[INFO] processing image 9542/9955
[INFO] processing image 9543/9955
[INFO] processing image 9544/9955
[INFO] processing image 9545/9955
[INFO] processing image 9546/9955
[INFO] processing image 9547/9955
[INFO] processing image 9548/9955
[INFO] processing image 9549/9955
[INFO] processing image 9550/9955
[INFO] processing image 9551/9955
[INFO] processing image 9552/9955
[INFO] processing image 9553/9955
[INFO] processing image 9554/9955
[INFO] processing image 9555/9955
[INFO] processing image 9556/9955
[INFO] processing image 9557/9955
[INFO] processing image 9558/9955
[INFO] processing image 9559/9955
[INFO] processing image 9560/9955
[INFO] processing image 9561/9955
[INFO] processing image 9562/9955
[INFO] processing image 9563/9955
[INFO] processing image 9564/9955
[INFO] processing image 9565/9955
[INFO] processing image 9566/9955
[INFO] processing image 9567/9955
[INFO] processing image 9568/9955
[INFO] processing image 9569/9955
[INFO] processing image 9570/9955
[INFO] processing image 9571/9955
[INFO] processing image 9572/9955
[INFO] processing image 9573/9955
[INFO] processing image 9574/9955
[INFO] processing image 9575/9955
[INFO] processing image 9576/9955
[INFO] processing image 9577/9955
[INFO] processing image 9578/9955
[INFO] processing image 9579/9955
[INFO] processing image 9580/9955
[INFO] processing image 9581/9955
[INFO] processing image 9582/9955
[INFO] processing image 9583/9955
[INFO] processing image 9584/9955
[INFO] processing image 9585/9955
[INFO] processing image 9586/9955
[INFO] processing image 9587/9955
[INFO] processing image 9588/9955
[INFO] processing image 9589/9955
[INFO] processing image 9590/9955
[INFO] processing image 9591/9955
[INFO] processing image 9592/9955
[INFO] processing image 9593/9955
[INFO] processing image 9594/9955
[INFO] processing image 9595/9955
[INFO] processing image 9596/9955
[INFO] processing image 9597/9955
[INFO] processing image 9598/9955
[INFO] processing image 9599/9955
[INFO] processing image 9600/9955
[INFO] processing image 9601/9955
[INFO] processing image 9602/9955
[INFO] processing image 9603/9955
[INFO] processing image 9604/9955
[INFO] processing image 9605/9955
[INFO] processing image 9606/9955
[INFO] processing image 9607/9955
[INFO] processing image 9608/9955
[INFO] processing image 9609/9955
[INFO] processing image 9610/9955
[INFO] processing image 9611/9955
[INFO] processing image 9612/9955
[INFO] processing image 9613/9955
[INFO] processing image 9614/9955
[INFO] processing image 9615/9955
[INFO] processing image 9616/9955
[INFO] processing image 9617/9955
[INFO] processing image 9618/9955
[INFO] processing image 9619/9955
[INFO] processing image 9620/9955
[INFO] processing image 9621/9955
[INFO] processing image 9622/9955
[INFO] processing image 9623/9955
[INFO] processing image 9624/9955
[INFO] processing image 9625/9955
[INFO] processing image 9626/9955
[INFO] processing image 9627/9955
[INFO] processing image 9628/9955
[INFO] processing image 9629/9955
[INFO] processing image 9630/9955
[INFO] processing image 9631/9955
[INFO] processing image 9632/9955
[INFO] processing image 9633/9955
[INFO] processing image 9634/9955
[INFO] processing image 9635/9955
[INFO] processing image 9636/9955
[INFO] processing image 9637/9955
[INFO] processing image 9638/9955
[INFO] processing image 9639/9955
[INFO] processing image 9640/9955
[INFO] processing image 9641/9955
[INFO] processing image 9642/9955
[INFO] processing image 9643/9955
[INFO] processing image 9644/9955
[INFO] processing image 9645/9955
[INFO] processing image 9646/9955
[INFO] processing image 9647/9955
[INFO] processing image 9648/9955
[INFO] processing image 9649/9955
[INFO] processing image 9650/9955
[INFO] processing image 9651/9955
[INFO] processing image 9652/9955
[INFO] processing image 9653/9955
[INFO] processing image 9654/9955
[INFO] processing image 9655/9955
[INFO] processing image 9656/9955
[INFO] processing image 9657/9955
[INFO] processing image 9658/9955
[INFO] processing image 9659/9955
[INFO] processing image 9660/9955
[INFO] processing image 9661/9955
[INFO] processing image 9662/9955
[INFO] processing image 9663/9955
[INFO] processing image 9664/9955
[INFO] processing image 9665/9955
[INFO] processing image 9666/9955
[INFO] processing image 9667/9955
[INFO] processing image 9668/9955
[INFO] processing image 9669/9955
[INFO] processing image 9670/9955
[INFO] processing image 9671/9955
[INFO] processing image 9672/9955
[INFO] processing image 9673/9955
[INFO] processing image 9674/9955
[INFO] processing image 9675/9955
[INFO] processing image 9676/9955
[INFO] processing image 9677/9955
[INFO] processing image 9678/9955
[INFO] processing image 9679/9955
[INFO] processing image 9680/9955
[INFO] processing image 9681/9955
[INFO] processing image 9682/9955
[INFO] processing image 9683/9955
[INFO] processing image 9684/9955
[INFO] processing image 9685/9955
[INFO] processing image 9686/9955
[INFO] processing image 9687/9955
[INFO] processing image 9688/9955
[INFO] processing image 9689/9955
[INFO] processing image 9690/9955
[INFO] processing image 9691/9955
[INFO] processing image 9692/9955
[INFO] processing image 9693/9955
[INFO] processing image 9694/9955
[INFO] processing image 9695/9955
[INFO] processing image 9696/9955
[INFO] processing image 9697/9955
[INFO] processing image 9698/9955
[INFO] processing image 9699/9955
[INFO] processing image 9700/9955
[INFO] processing image 9701/9955
[INFO] processing image 9702/9955
[INFO] processing image 9703/9955
[INFO] processing image 9704/9955
[INFO] processing image 9705/9955
[INFO] processing image 9706/9955
[INFO] processing image 9707/9955
[INFO] processing image 9708/9955
[INFO] processing image 9709/9955
[INFO] processing image 9710/9955
[INFO] processing image 9711/9955
[INFO] processing image 9712/9955
[INFO] processing image 9713/9955
[INFO] processing image 9714/9955
[INFO] processing image 9715/9955
[INFO] processing image 9716/9955
[INFO] processing image 9717/9955
[INFO] processing image 9718/9955
[INFO] processing image 9719/9955
[INFO] processing image 9720/9955
[INFO] processing image 9721/9955
[INFO] processing image 9722/9955
[INFO] processing image 9723/9955
[INFO] processing image 9724/9955
[INFO] processing image 9725/9955
[INFO] processing image 9726/9955
[INFO] processing image 9727/9955
[INFO] processing image 9728/9955
[INFO] processing image 9729/9955
[INFO] processing image 9730/9955
[INFO] processing image 9731/9955
[INFO] processing image 9732/9955
[INFO] processing image 9733/9955
[INFO] processing image 9734/9955
[INFO] processing image 9735/9955
[INFO] processing image 9736/9955
[INFO] processing image 9737/9955
[INFO] processing image 9738/9955
[INFO] processing image 9739/9955
[INFO] processing image 9740/9955
[INFO] processing image 9741/9955
[INFO] processing image 9742/9955
[INFO] processing image 9743/9955
[INFO] processing image 9744/9955
[INFO] processing image 9745/9955
[INFO] processing image 9746/9955
[INFO] processing image 9747/9955
[INFO] processing image 9748/9955
[INFO] processing image 9749/9955
[INFO] processing image 9750/9955
[INFO] processing image 9751/9955
[INFO] processing image 9752/9955
[INFO] processing image 9753/9955
[INFO] processing image 9754/9955
[INFO] processing image 9755/9955
[INFO] processing image 9756/9955
[INFO] processing image 9757/9955
[INFO] processing image 9758/9955
[INFO] processing image 9759/9955
[INFO] processing image 9760/9955
[INFO] processing image 9761/9955
[INFO] processing image 9762/9955
[INFO] processing image 9763/9955
[INFO] processing image 9764/9955
[INFO] processing image 9765/9955
[INFO] processing image 9766/9955
[INFO] processing image 9767/9955
[INFO] processing image 9768/9955
[INFO] processing image 9769/9955
[INFO] processing image 9770/9955
[INFO] processing image 9771/9955
[INFO] processing image 9772/9955
[INFO] processing image 9773/9955
[INFO] processing image 9774/9955
[INFO] processing image 9775/9955
[INFO] processing image 9776/9955
[INFO] processing image 9777/9955
[INFO] processing image 9778/9955
[INFO] processing image 9779/9955
[INFO] processing image 9780/9955
[INFO] processing image 9781/9955
[INFO] processing image 9782/9955
[INFO] processing image 9783/9955
[INFO] processing image 9784/9955
[INFO] processing image 9785/9955
[INFO] processing image 9786/9955
[INFO] processing image 9787/9955
[INFO] processing image 9788/9955
[INFO] processing image 9789/9955
[INFO] processing image 9790/9955
[INFO] processing image 9791/9955
[INFO] processing image 9792/9955
[INFO] processing image 9793/9955
[INFO] processing image 9794/9955
[INFO] processing image 9795/9955
[INFO] processing image 9796/9955
[INFO] processing image 9797/9955
[INFO] processing image 9798/9955
[INFO] processing image 9799/9955
[INFO] processing image 9800/9955
[INFO] processing image 9801/9955
[INFO] processing image 9802/9955
[INFO] processing image 9803/9955
[INFO] processing image 9804/9955
[INFO] processing image 9805/9955
[INFO] processing image 9806/9955
[INFO] processing image 9807/9955
[INFO] processing image 9808/9955
[INFO] processing image 9809/9955
[INFO] processing image 9810/9955
[INFO] processing image 9811/9955
[INFO] processing image 9812/9955
[INFO] processing image 9813/9955
[INFO] processing image 9814/9955
[INFO] processing image 9815/9955
[INFO] processing image 9816/9955
[INFO] processing image 9817/9955
[INFO] processing image 9818/9955
[INFO] processing image 9819/9955
[INFO] processing image 9820/9955
[INFO] processing image 9821/9955
[INFO] processing image 9822/9955
[INFO] processing image 9823/9955
[INFO] processing image 9824/9955
[INFO] processing image 9825/9955
[INFO] processing image 9826/9955
[INFO] processing image 9827/9955
[INFO] processing image 9828/9955
[INFO] processing image 9829/9955
[INFO] processing image 9830/9955
[INFO] processing image 9831/9955
[INFO] processing image 9832/9955
[INFO] processing image 9833/9955
[INFO] processing image 9834/9955
[INFO] processing image 9835/9955
[INFO] processing image 9836/9955
[INFO] processing image 9837/9955
[INFO] processing image 9838/9955
[INFO] processing image 9839/9955
[INFO] processing image 9840/9955
[INFO] processing image 9841/9955
[INFO] processing image 9842/9955
[INFO] processing image 9843/9955
[INFO] processing image 9844/9955
[INFO] processing image 9845/9955
[INFO] processing image 9846/9955
[INFO] processing image 9847/9955
[INFO] processing image 9848/9955
[INFO] processing image 9849/9955
[INFO] processing image 9850/9955
[INFO] processing image 9851/9955
[INFO] processing image 9852/9955
[INFO] processing image 9853/9955
[INFO] processing image 9854/9955
[INFO] processing image 9855/9955
[INFO] processing image 9856/9955
[INFO] processing image 9857/9955
[INFO] processing image 9858/9955
[INFO] processing image 9859/9955
[INFO] processing image 9860/9955
[INFO] processing image 9861/9955
[INFO] processing image 9862/9955
[INFO] processing image 9863/9955
[INFO] processing image 9864/9955
[INFO] processing image 9865/9955
[INFO] processing image 9866/9955
[INFO] processing image 9867/9955
[INFO] processing image 9868/9955
[INFO] processing image 9869/9955
[INFO] processing image 9870/9955
[INFO] processing image 9871/9955
[INFO] processing image 9872/9955
[INFO] processing image 9873/9955
[INFO] processing image 9874/9955
[INFO] processing image 9875/9955
[INFO] processing image 9876/9955
[INFO] processing image 9877/9955
[INFO] processing image 9878/9955
[INFO] processing image 9879/9955
[INFO] processing image 9880/9955
[INFO] processing image 9881/9955
[INFO] processing image 9882/9955
[INFO] processing image 9883/9955
[INFO] processing image 9884/9955
[INFO] processing image 9885/9955
[INFO] processing image 9886/9955
[INFO] processing image 9887/9955
[INFO] processing image 9888/9955
[INFO] processing image 9889/9955
[INFO] processing image 9890/9955
[INFO] processing image 9891/9955
[INFO] processing image 9892/9955
[INFO] processing image 9893/9955
[INFO] processing image 9894/9955
[INFO] processing image 9895/9955
[INFO] processing image 9896/9955
[INFO] processing image 9897/9955
[INFO] processing image 9898/9955
[INFO] processing image 9899/9955
[INFO] processing image 9900/9955
[INFO] processing image 9901/9955
[INFO] processing image 9902/9955
[INFO] processing image 9903/9955
[INFO] processing image 9904/9955
[INFO] processing image 9905/9955
[INFO] processing image 9906/9955
[INFO] processing image 9907/9955
[INFO] processing image 9908/9955
[INFO] processing image 9909/9955
[INFO] processing image 9910/9955
[INFO] processing image 9911/9955
[INFO] processing image 9912/9955
[INFO] processing image 9913/9955
[INFO] processing image 9914/9955
[INFO] processing image 9915/9955
[INFO] processing image 9916/9955
[INFO] processing image 9917/9955
[INFO] processing image 9918/9955
[INFO] processing image 9919/9955
[INFO] processing image 9920/9955
[INFO] processing image 9921/9955
[INFO] processing image 9922/9955
[INFO] processing image 9923/9955
[INFO] processing image 9924/9955
[INFO] processing image 9925/9955
[INFO] processing image 9926/9955
[INFO] processing image 9927/9955
[INFO] processing image 9928/9955
[INFO] processing image 9929/9955
[INFO] processing image 9930/9955
[INFO] processing image 9931/9955
[INFO] processing image 9932/9955
[INFO] processing image 9933/9955
[INFO] processing image 9934/9955
[INFO] processing image 9935/9955
[INFO] processing image 9936/9955
[INFO] processing image 9937/9955
[INFO] processing image 9938/9955
[INFO] processing image 9939/9955
[INFO] processing image 9940/9955
[INFO] processing image 9941/9955
[INFO] processing image 9942/9955
[INFO] processing image 9943/9955
[INFO] processing image 9944/9955
[INFO] processing image 9945/9955
[INFO] processing image 9946/9955
[INFO] processing image 9947/9955
[INFO] processing image 9948/9955
[INFO] processing image 9949/9955
[INFO] processing image 9950/9955
[INFO] processing image 9951/9955
[INFO] processing image 9952/9955
[INFO] processing image 9953/9955
[INFO] processing image 9954/9955
[INFO] processing image 9955/9955
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now, folder <code>extracted_letter_images</code> should contain 32 folders, each storing the corresponding letter images</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-2:-Train-the-neural-network-to-recognize-single-letters">Step 2: Train the neural network to recognize single letters<a class="anchor-link" href="#Step-2:-Train-the-neural-network-to-recognize-single-letters">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Since input layer of a neural network model takes images of fixed size (usually square), we need to resize images first.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">letter_image_file</span> <span class="o">=</span> <span class="s1">&#39;extracted_letter_images/2/000001.png&#39;</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">letter_image_file</span><span class="p">)</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2GRAY</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> 
<span class="p">(</span><span class="n">h</span><span class="p">,</span> <span class="n">w</span><span class="p">)</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="c1"># note that cv.imread gets an array of h x w, h goes first</span>
<span class="c1"># add [:2] so that even if color image will work, not needed here though</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(16, 11)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
ACMnxky5h+HOAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Since <code>h &gt; w</code>, we make sure <code>h</code> fits in our desired height value, e.g., 20:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">imutils</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">imutils</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<span class="c1"># imutils.resize maintains the aspect ratio</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
rkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we pad along width to make the image square, i.e., 20 x 20:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># determine the padding values for the width (= 20)</span>
<span class="c1"># to obtain the target dimensions</span>
<span class="n">padW</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="mi">20</span> <span class="o">-</span> <span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">)</span> <span class="c1"># may have rounding</span>

<span class="c1"># pad the image</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">copyMakeBorder</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">padW</span><span class="p">,</span> <span class="n">padW</span><span class="p">,</span>
        <span class="n">cv2</span><span class="o">.</span><span class="n">BORDER_REPLICATE</span><span class="p">)</span>

<span class="c1"># apply one more resizing to handle any rounding issues</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">))</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
baYWn0H8maSfJtaFpIdtP217YQ32BaCOqppqbfvvJXVL+lGi5MyI6LI9QdIK2+uKM5KybS2UtFCS
pk1mBviW7vzp0zft+GR27VMPnZxdO+X53dm1r547Krv2W5+8K7v2U4duza7tifzp07tiT1bdSOf/
X+xw+33mX/ER2V4g6QJJX4yI0n6bEdFVPG6TtETSrNT2aL0HNJ+KAsL2eZK+JumiiNiVqBlte0zf
c/W23Xu2rBZAc8r5mrOs7d4iSWPUe9mw2vZNRe3RtpcVb50o6QnbayQ9KenBiHhoSI4CwJA44AVW
ou3ebYnaLklzi+cbJJ1S1egANFT7faoCoGYICABJBASAJAICQBIBASCJgACQxJzmJrXsd8dn1/7k
Z5/Irv3Ikh0HLip0nX1Edu1XL74/u3be6Neya98tnaNbbn13/l2thyuv9veGO3ubHW34+7b9jghA
zRAQAJIICABJBASAJAICQBIBASCJgACQREAASCIgACQxk7KO/um1E7Jrf/jjc7Jrj1/+dnbtKxfm
z4686osPZNdeOXZzdq00PLvy3rcnZdd+4+kLs2sPOfS9rLr7Tr05e5vHDc8/rlbBGQSApEpb733d
9ubifpSrbc9NvPc82y/aXm/72loOHMDQq7T1niR9t2ipNzMilg1cabtD0g2Szpd0kqTLbJ9UzWAB
1FdFrfcyzZK0PiI2RMQeSfdImlfBdgA0SDWfQVxddPdebHtcyfrJkjb1e91ZLAPQIioNiBslHSdp
pqQtkr5TUlP2h/TJv+63vdD2Stsrt7/eU+GwANRSRQEREVsjoici9kq6ReUt9TolTe33eoqkrv1s
k9Z7QJOptPVe/y+nP6fylnpPSZph+1jbIyTNl7S0kv0BaIwDTpQqWu/NljTedqek6yXNtj1TvZcM
GyVdUdQeLenWiJgbEd22r5a0XFKHpMUR8dyQHAWAITFkrfeK18sk7fMVKIDWwFTrGng/8j5UvXXV
J7O3ecIDb2bX7l39fHbt9N/lT/e+85XPZNfePD7/arVnVHapRr6Rf9faSdvzb1rbOSdvWvSUYSOz
t9mOmGoNIImAAJBEQABIIiAAJBEQAJIICABJBASAJAICQBIBASCJgACQxFTrOjr1uFeya9fMn5Fd
O2rOH2bX9gzixssxVDdpzp89rffGlt1WJFE7Lv82AROnbcuqG+n2u1P1YHAGASCJgACQREAASCIg
ACQREACSCAgASTn3pFws6QJJ2yLi5GLZvZL6bk00VtKbETGz5L0bJb0tqUdSd0ScVqNxA6iDnHkQ
t0taJOkHfQsi4tK+57a/I2nnft5/VkS8VukAATROzk1rH7M9vWydbUv6gqSzazssAM2g2s8g/kjS
1oh4ObE+JD1s+2nbC6vcF4A6q3aq9WWS7t7P+jMjosv2BEkrbK8rmgHvowiQhZI0bXJrzQAf7rwp
vrdMz+8btGlqfnZ3dR+eXfvbQdRu7x6Tv933BrHdPYdl1+7qHpFdO6qjO7v2ovG/yq49mFV8BmF7
mKSLJd2bqin6ZCgitklaovIWfX21tN4Dmkw1lxifkrQuIjrLVtoebXtM33NJc1Teog9AkzpgQBSt
934u6QTbnbYvL1bN14DLC9tH2+7rpDVR0hO210h6UtKDEfFQ7YYOYKhV2npPEfGlkmUftN6LiA2S
TqlyfAAaiJmUAJIICABJBASAJAICQBIBASCJgACQ1FpzmlvcuI5DB1Gbv92PjXhvEKPIu5vz4GvR
jjiDAJBEQABIIiAAJBEQAJIICABJBASAJAICQBIBASCJgACQREAASHJENHoM+7C9XdIrAxaPl9SO
DXja9bik9j22djiuYyLiqAMVNWVAlLG9sh1b97XrcUnte2ztelxluMQAkERAAEhqpYC4udEDGCLt
elxS+x5bux7XPlrmMwgA9ddKZxAA6qwlAsL2ebZftL3e9rWNHk+t2N5oe63t1bZXNno81bC92PY2
28/2W3aE7RW2Xy4exzVyjJVIHNfXbW8ufm6rbc9t5BiHUtMHhO0OSTdIOl/SSZIus31SY0dVU2dF
xMw2+NrsdknnDVh2raRHImKGpEeK163mdu17XJL03eLnNjMilpWsbwtNHxDq7Qi+PiI2RMQeSfdI
mtfgMWGAiHhM0o4Bi+dJuqN4foekz9Z1UDWQOK6DRisExGRJm/q97iyWtYOQ9LDtp20vbPRghsDE
iNgiScXjhAaPp5autv1McQnScpdOuVohIFyyrF2+ejkzIk5V7+XTVbb/uNEDQpYbJR0naaakLZK+
09jhDJ1WCIhOSVP7vZ4iqatBY6mpohu6ImKbpCXqvZxqJ1ttT5Kk4rEt7qMfEVsjoici9kq6Re33
c/tAKwTEU5Jm2D7W9ghJ8yUtbfCYqmZ7tO0xfc8lzZH07P7f1XKWSlpQPF8g6f4GjqVm+kKv8Dm1
38/tA03fOCcium1fLWm5pA5JiyPiuQYPqxYmSlpiW+r9OdwVEQ81dkiVs323pNmSxtvulHS9pG9K
+k/bl0t6VdLnGzfCyiSOa7btmeq91N0o6YqGDXCIMZMSQFIrXGIAaBACAkASAQEgiYAAkERAAEgi
IAAkERAAkggIAEn/B+GCyGKUWMshAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Using what you learned, now write a function to resize images. Note that you also need to handle the possible case <code>h &lt; w</code>:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">resize_to_fit</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">):</span>
    

    <span class="p">(</span><span class="n">h</span><span class="p">,</span> <span class="n">w</span><span class="p">)</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> 

    <span class="k">if</span> <span class="n">w</span> <span class="o">&gt;</span> <span class="n">h</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">imutils</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">imutils</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="n">width</span><span class="p">)</span>

   
    <span class="n">padW</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="n">width</span> <span class="o">-</span> <span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">)</span>
    <span class="n">padH</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="n">width</span> <span class="o">-</span> <span class="n">image</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">)</span>

    <span class="c1"># pad the image then apply one more resizing to handle any</span>
    <span class="c1"># rounding issues</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">copyMakeBorder</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">padH</span><span class="p">,</span> <span class="n">padH</span><span class="p">,</span> <span class="n">padW</span><span class="p">,</span> <span class="n">padW</span><span class="p">,</span>
        <span class="n">cv2</span><span class="o">.</span><span class="n">BORDER_REPLICATE</span><span class="p">)</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="p">(</span><span class="mi">20</span><span class="p">,</span><span class="mi">20</span><span class="p">))</span>

    <span class="c1"># return the pre-processed image</span>
    <span class="k">return</span> <span class="n">image</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Prepare the training and validating datasets:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">imutils</span> <span class="k">import</span> <span class="n">paths</span>

<span class="c1"># initialize the data and labels</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">labels</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">progress_folder</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<span class="n">LETTER_IMAGES_FOLDER</span> <span class="o">=</span> <span class="s2">&quot;extracted_letter_images&quot;</span>

<span class="c1"># loop over the input images</span>
<span class="c1"># imutils.paths.list_images will list all images in the 32 subfolders</span>
<span class="k">for</span> <span class="n">image_file</span> <span class="ow">in</span> <span class="n">paths</span><span class="o">.</span><span class="n">list_images</span><span class="p">(</span><span class="n">LETTER_IMAGES_FOLDER</span><span class="p">):</span>
    <span class="c1"># Load the image and convert it to grayscale</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">imread</span><span class="p">(</span><span class="n">image_file</span><span class="p">)</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2GRAY</span><span class="p">)</span>

    <span class="c1"># Resize the letter so it fits in a 20x20 pixel box</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">resize_to_fit</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>

    <span class="c1"># Add a third channel dimension to the image to make Keras happy</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">expand_dims</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

    <span class="c1"># Grab the name of the letter based on the folder it was in</span>
    <span class="n">label</span> <span class="o">=</span> <span class="n">image_file</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">sep</span><span class="p">)[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
    <span class="c1"># extracted_letter_images/2/000001.png, after split</span>
    <span class="c1"># extracted_letter_images, 2, 000001.png</span>
    <span class="c1"># so 2 is the 2nd last, accessed using index -2</span>
    
    <span class="k">if</span> <span class="n">label</span> <span class="o">!=</span> <span class="n">progress_folder</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Processing Folder&#39;</span><span class="p">,</span> <span class="n">label</span><span class="p">)</span>
        <span class="n">progress_folder</span> <span class="o">=</span> <span class="n">label</span>
    
    <span class="c1"># Add the letter image and it&#39;s label to our training data</span>
    <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
    <span class="n">labels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Processing Folder 2
Processing Folder 3
Processing Folder 4
Processing Folder 5
Processing Folder 6
Processing Folder 7
Processing Folder 8
Processing Folder 9
Processing Folder A
Processing Folder B
Processing Folder C
Processing Folder D
Processing Folder E
Processing Folder F
Processing Folder G
Processing Folder H
Processing Folder J
Processing Folder K
Processing Folder L
Processing Folder M
Processing Folder N
Processing Folder P
Processing Folder Q
Processing Folder R
Processing Folder S
Processing Folder T
Processing Folder U
Processing Folder V
Processing Folder W
Processing Folder X
Processing Folder Y
Processing Folder Z
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Convert lists into NumPy arrays as required by Keras for input + data normalization:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># scale the raw pixel intensities to the range [0, 1] (this is important!!!)</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="s2">&quot;float&quot;</span><span class="p">)</span> <span class="o">/</span> <span class="mf">255.0</span>

<span class="c1"># you may also use std rather than 255, and center the data by mean as follows:</span>
<span class="c1">#data = (np.array(data, dtype=&quot;float&quot;) - data.mean()) / data.std()</span>
<span class="c1"># in this case you need to remember the mean and std for use during testing later</span>

<span class="c1"># scaling is not needed if you use BatchNormalization after Conv2D and before Activation</span>

<span class="n">labels</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Split into training and validation datasets:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="k">import</span> <span class="n">LabelBinarizer</span>

<span class="c1"># Convert the labels (letters) into one-hot encodings that Keras can work with</span>
<span class="n">lb</span> <span class="o">=</span> <span class="n">LabelBinarizer</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">lb</span><span class="o">.</span><span class="n">classes_</span><span class="p">)</span>
<span class="n">labels</span> <span class="o">=</span> <span class="n">lb</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;2&#39; &#39;3&#39; &#39;4&#39; &#39;5&#39; &#39;6&#39; &#39;7&#39; &#39;8&#39; &#39;9&#39; &#39;A&#39; &#39;B&#39; &#39;C&#39; &#39;D&#39; &#39;E&#39; &#39;F&#39; &#39;G&#39; &#39;H&#39; &#39;J&#39; &#39;K&#39;
 &#39;L&#39; &#39;M&#39; &#39;N&#39; &#39;P&#39; &#39;Q&#39; &#39;R&#39; &#39;S&#39; &#39;T&#39; &#39;U&#39; &#39;V&#39; &#39;W&#39; &#39;X&#39; &#39;Y&#39; &#39;Z&#39;]

[[1 0 0 ... 0 0 0]
 [1 0 0 ... 0 0 0]
 [1 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 1]
 [0 0 0 ... 0 0 1]
 [0 0 0 ... 0 0 1]]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pickle</span>

<span class="n">MODEL_LABELS_FILENAME</span> <span class="o">=</span> <span class="s2">&quot;model_labels.dat&quot;</span>

<span class="c1"># Save the mapping from labels to one-hot encodings.</span>
<span class="c1"># We&#39;ll need this later when we use the model to decode what it&#39;s predictions mean</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">MODEL_LABELS_FILENAME</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">lb</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we are ready to train it using Keras. We’ll use a simple convolutional neural network architecture with two convolutional layers and two fully-connected layers:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[165]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">tensorflow.python.keras.backend</span> <span class="k">import</span> <span class="n">clear_session</span>
<span class="kn">from</span> <span class="nn">tensorflow.python.keras.models</span> <span class="k">import</span> <span class="n">Sequential</span>
<span class="kn">from</span> <span class="nn">tensorflow.python.keras.layers</span> <span class="k">import</span> <span class="n">Conv2D</span><span class="p">,</span> <span class="n">MaxPooling2D</span><span class="p">,</span> <span class="n">Flatten</span><span class="p">,</span> <span class="n">Dense</span>

<span class="n">clear_session</span><span class="p">()</span> <span class="c1"># free existing Keras models</span>

<span class="c1"># Build the neural network!</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">Sequential</span><span class="p">()</span>

<span class="c1"># First convolutional layer with max pooling</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Conv2D</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">),</span> <span class="n">padding</span><span class="o">=</span><span class="s2">&quot;same&quot;</span><span class="p">,</span> <span class="n">input_shape</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">MaxPooling2D</span><span class="p">(</span><span class="n">pool_size</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">strides</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>

<span class="c1"># Second convolutional layer with max pooling</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Conv2D</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="n">padding</span><span class="o">=</span><span class="s2">&quot;same&quot;</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">MaxPooling2D</span><span class="p">(</span><span class="n">pool_size</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">strides</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>

<span class="c1"># Hidden layer with 500 nodes</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Flatten</span><span class="p">())</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>

<span class="c1"># Output layer with 32 nodes (one for each possible letter/number we predict)</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">32</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;softmax&quot;</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">model</span><span class="o">.</span><span class="n">summary</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 20, 20, 20)        520       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 10, 10, 20)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 10, 10, 50)        9050      
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 5, 5, 50)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 1250)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 500)               625500    
_________________________________________________________________
dense_2 (Dense)              (None, 32)                16032     
=================================================================
Total params: 651,102
Trainable params: 651,102
Non-trainable params: 0
_________________________________________________________________
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[166]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">keras.utils.vis_utils</span> <span class="k">import</span> <span class="n">plot_model</span>

<span class="n">MODEL_PLOT_FILE</span> <span class="o">=</span> <span class="s1">&#39;model_plot.png&#39;</span>
<span class="n">plot_model</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">to_file</span><span class="o">=</span><span class="n">MODEL_PLOT_FILE</span><span class="p">,</span> <span class="n">show_shapes</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">show_layer_names</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">display</span><span class="p">(</span><span class="n">Image</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="n">MODEL_PLOT_FILE</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
IiIiRwwWiIiIyJFtA0c5TSkRkR/kMLT8bXHn2rVr2LFjR9DZoB7i9LfZMILj9evX8dRTT7U9U0RE
RBQu9957Lz799FPz4hMNwQIR9S4O905EFjjcMxERETljsEBERESOGCwQERGRIwYLRERE5IjBAhER
ETlisEBERESOGCwQERGRIwYLRERE5IjBAhERETlisEBERESOGCwQERGRIwYLRERE5IjBAhERETli
sEBERESOGCwQERGRIwYLRERE5IjBAhERETlisEBERESOGCwQERGRIwYLRERE5IjBAhERETlisEBE
RESOGCwQERGRIwYLRERE5IjBAhERETlisEBERESOGCwQERGRIwYLRERE5IjBAhERETlisEBERESO
GCwQERGRIwYLRERE5IjBAhERETnaHnQGiCg47777Ln7+85/r7wuFAgDgb/7mb+q2+9M//VN87Wtf
62jeiCg8FCGECDoTRBQMRVEAAPfdd5/tNp9++in+6q/+qiGAIKKecYLVEEQ97MSJE7j33nvx6aef
2r4A4OjRowHnlIiCxGCBqIeNjo7is88+c9zmwQcfxDPPPNOhHBFRGDFYIOph3/jGN7Br1y7b9ffe
ey/Gx8dxzz38qSDqZfwFIOphiqLglVdewY4dOyzXf/bZZxgbG+twrogobBgsEPW4aDSK27dvW677
f//v/+HJJ5/scI6IKGwYLBD1uK9//ev4vd/7vYblO3bswF/8xV90PkNEFDoMFogIr776akNVxO3b
t1kFQUQAGCwQEYCxsTH8+te/1t8rioI/+IM/sCxxIKLew2CBiPDII49g7969+iBN27Ztw6uvvhpw
rogoLBgsEBEAYGJiAtu2bQMA3LlzB6OjowHniIjCgsECEQEAXnrpJfzmN78BADzzzDOO4y8QUW9h
sEBEADZGapTdJMfHxwPODRGFSU9NJBWPx/HXf/3XQWeDiIi63LVr17Bv376gs9EpJ3pqiuqf//zn
2LFjB1KpVNBZIbL03nvv4Yc//CHefffdQNIXQuD//u//0NfXF0j6rfjhD38IAHj99dcDzgn1mmPH
juE//uM/eilYQE8FCwAwMjKCkZGRoLNBZEmOpMhrtLkf/ehHAHiuiDqBbRaIiIjIEYMFIiIicsRg
gYiIiBwxWCAiIiJHDBaIiIjIEYMFoi1qZmYGMzMzQWcjtCqVCmZnZ4POBnXY7OwsarVa0NnoOgwW
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
um5Kr1ar1Z1rL+nF4/FN56MXMFgg6nJHjhyBqqo4d+6c/kR18eJFNzW0OwAAIABJREFUaJqGgwcP
6tvJJzB5ozd2PZOj4BmfzMw3KtmdsFarYXFxEaqq1hX7et1/J7tO7t69G0BjsCDPm1UpwejoqOUN
xc15N+5PpmlMW65//vnnAWy0Uejv74eiKBgcHNRvhLJLpZveEcb9m49zaGgIyWQS58+fR61WQ61W
w/nz55FMJut6EIQxvUwmU9eddH19HVeuXKm7xt2mJz8PAPv27Wt6jAT2hiAKE6+DMpXLZZFMJusG
FqpWq3XblEolvZW/HNhGVVWRTqf1Fv2yl0M8HteXyX0WCgX988lk0rf9x+NxT63+vfw9l8vlhkF7
5PEZX1ZUVbXcn9N5t9qvXVqlUklv4a9pmiiVSvq6eDwuNE2zzIOR1bFYHU82mxUAhKqqYnl5uWF9
GNOT+5DXj9OgTs3SE+JuzxVjbxa30IO9IRQhemfw//HxcQBAKpUKOCdE1paWljA+Ph6qOTlky/ww
5Qnw/vcsSzROnjzZ0udqtVrgQwNHIhFks1mm54OZmRn09/e3fB0AG38TqVRKr4rqASdYDUFEPSUW
i+Hy5cuWIwA6CTpQyOfzmJ6eZno+KBaLKBaLiMViHUlvK2CwQES2zEMXbwVyHIVz5875PkJiu6ys
rOCBBx7A/v37md4mra2tYW5uDgsLC4EHgN2Es04Ska3BwcG6/4etKsKrgYEBLC4uYmFhQR9gKsyM
jfiY3ubkcjmcPn061LOHhhGDBSKytVWCAyt9fX2e6qupu/E794bVEEREROSIwQIRERE5YrBARERE
jhgsEBERkaOea+C4tLSE27dvB50NIktyCNpjx44FnJPwu3btGgCeK6JO6KkRHHO5HBYXF4POBlFo
ffzxx/jpT3+KQ4cOBZ0VotDatm0b3nrrLTz44INBZ6VTTvRUsEBEzsI43DQRBY7DPRMREZEzBgtE
RETkiMECEREROWKwQERERI4YLBAREZEjBgtERETkiMECEREROWKwQERERI4YLBAREZEjBgtERETk
iMECEREROWKwQERERI4YLBAREZEjBgtERETkiMECEREROWKwQERERI4YLBAREZEjBgtERETkiMEC
EREROWKwQERERI4YLBAREZEjBgtERETkiMECEREROWKwQERERI4YLBAREZEjBgtERETkiMECERER
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
RK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Questions: (1) Why <code>conv2d_1</code> has 9050 parameters? (2) Why <code>dense</code> has 625500 parameters?</p>
<p>Hint: self-study <a href="http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf">http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf</a></p>
<p><strong>Type Your Answer Here:</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>(1 )Here,conv2d_1 has 9050 parameters because it is the 3x3 dimensional matrix during max pooling for feature map.Here,we had flatten the nodes into one dimensional vector to get the output.
(2)Dense has 625500 parameters because of one huge dimensional vector for which all the nodes are flattened.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now, let us do the actual training:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[167]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Ask Keras to build the TensorFlow model behind the scenes</span>
<span class="n">model</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">loss</span><span class="o">=</span><span class="s2">&quot;categorical_crossentropy&quot;</span><span class="p">,</span> <span class="n">optimizer</span><span class="o">=</span><span class="s2">&quot;adam&quot;</span><span class="p">,</span> <span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;accuracy&quot;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[168]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Train the neural network, 20% of the data is used for validation</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">validation_split</span><span class="o">=</span><span class="mf">0.20</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span> <span class="n">epochs</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Train on 31803 samples, validate on 7951 samples
Epoch 1/10
31803/31803 [==============================] - 57s 2ms/step - loss: 2.6805 - acc: 0.2368 - val_loss: 15.0576 - val_acc: 0.0416
Epoch 2/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.3323 - acc: 0.9583 - val_loss: 14.9830 - val_acc: 0.0702
Epoch 3/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.2351 - acc: 0.9707 - val_loss: 14.9352 - val_acc: 0.0704
Epoch 4/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1995 - acc: 0.9731 - val_loss: 14.7333 - val_acc: 0.0703
Epoch 5/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1813 - acc: 0.9751 - val_loss: 14.7662 - val_acc: 0.0704
Epoch 6/10
31803/31803 [==============================] - 43s 1ms/step - loss: 0.1689 - acc: 0.9760 - val_loss: 14.7392 - val_acc: 0.0706
Epoch 7/10
31803/31803 [==============================] - 43s 1ms/step - loss: 0.1585 - acc: 0.9769 - val_loss: 14.6094 - val_acc: 0.0706
Epoch 8/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1511 - acc: 0.9776 - val_loss: 14.7150 - val_acc: 0.0703
Epoch 9/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1447 - acc: 0.9787 - val_loss: 14.7369 - val_acc: 0.0706
Epoch 10/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1376 - acc: 0.9788 - val_loss: 14.7496 - val_acc: 0.0706
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[168]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;tensorflow.python.keras._impl.keras.callbacks.History at 0x2d7af8f6390&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Save the model for later use:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">MODEL_FILENAME</span> <span class="o">=</span> <span class="s2">&quot;captcha_model.hdf5&quot;</span>

<span class="c1"># Save the trained model to disk</span>
<span class="n">model</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">MODEL_FILENAME</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#See what will happen if you do not scale your data by 255.0?</span>
<span class="c1">#HINT: simply train again with data/255.0 instead of 255, and see how the loss and acc look like;</span>
<span class="c1">#      you need to recreate your model by running the cell containing clear_session() before</span>

<span class="c1">#[YOUR CODE HERE]</span>


<span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="s2">&quot;float&quot;</span><span class="p">)</span> <span class="o">/</span> <span class="mi">255</span>
<span class="n">labels</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>

<span class="n">lb</span> <span class="o">=</span> <span class="n">LabelBinarizer</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>
<span class="n">labels</span> <span class="o">=</span> <span class="n">lb</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">labels</span><span class="p">)</span>


<span class="kn">from</span> <span class="nn">tensorflow.python.keras.backend</span> <span class="k">import</span> <span class="n">clear_session</span>
<span class="kn">from</span> <span class="nn">tensorflow.python.keras.models</span> <span class="k">import</span> <span class="n">Sequential</span>
<span class="kn">from</span> <span class="nn">tensorflow.python.keras.layers</span> <span class="k">import</span> <span class="n">Conv2D</span><span class="p">,</span> <span class="n">MaxPooling2D</span><span class="p">,</span> <span class="n">Flatten</span><span class="p">,</span> <span class="n">Dense</span>

<span class="n">clear_session</span><span class="p">()</span> <span class="c1"># free existing Keras models</span>

<span class="c1"># Build the neural network!</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">Sequential</span><span class="p">()</span>

<span class="c1"># First convolutional layer with max pooling</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Conv2D</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">),</span> <span class="n">padding</span><span class="o">=</span><span class="s2">&quot;same&quot;</span><span class="p">,</span> <span class="n">input_shape</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">MaxPooling2D</span><span class="p">(</span><span class="n">pool_size</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">strides</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>

<span class="c1"># Second convolutional layer with max pooling</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Conv2D</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="n">padding</span><span class="o">=</span><span class="s2">&quot;same&quot;</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">MaxPooling2D</span><span class="p">(</span><span class="n">pool_size</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">strides</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>

<span class="c1"># Hidden layer with 500 nodes</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Flatten</span><span class="p">())</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;relu&quot;</span><span class="p">))</span>

<span class="c1"># Output layer with 32 nodes (one for each possible letter/number we predict)</span>
<span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">32</span><span class="p">,</span> <span class="n">activation</span><span class="o">=</span><span class="s2">&quot;softmax&quot;</span><span class="p">))</span>

<span class="c1"># Ask Keras to build the TensorFlow model behind the scenes</span>
<span class="n">model</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">loss</span><span class="o">=</span><span class="s2">&quot;categorical_crossentropy&quot;</span><span class="p">,</span> <span class="n">optimizer</span><span class="o">=</span><span class="s2">&quot;adam&quot;</span><span class="p">,</span> <span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;accuracy&quot;</span><span class="p">])</span>

<span class="c1"># Train the neural network, 20% of the data is used for validation</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">validation_split</span><span class="o">=</span><span class="mf">0.20</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span> <span class="n">epochs</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Train on 31803 samples, validate on 7951 samples
Epoch 1/10
31803/31803 [==============================] - 41s 1ms/step - loss: 1.9876 - acc: 0.4512 - val_loss: 14.9921 - val_acc: 0.0669
Epoch 2/10
31803/31803 [==============================] - 41s 1ms/step - loss: 0.2752 - acc: 0.9658 - val_loss: 14.9758 - val_acc: 0.0706
Epoch 3/10
31803/31803 [==============================] - 41s 1ms/step - loss: 0.2109 - acc: 0.9726 - val_loss: 14.9214 - val_acc: 0.0704
Epoch 4/10
31803/31803 [==============================] - 41s 1ms/step - loss: 0.1837 - acc: 0.9742 - val_loss: 14.7943 - val_acc: 0.0704
Epoch 5/10
31803/31803 [==============================] - 40s 1ms/step - loss: 0.1687 - acc: 0.9759 - val_loss: 14.8223 - val_acc: 0.0689
Epoch 6/10
31803/31803 [==============================] - 41s 1ms/step - loss: 0.1563 - acc: 0.9770 - val_loss: 14.7822 - val_acc: 0.0704
Epoch 7/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1481 - acc: 0.9778 - val_loss: 14.7409 - val_acc: 0.0704
Epoch 8/10
31803/31803 [==============================] - 41s 1ms/step - loss: 0.1400 - acc: 0.9787 - val_loss: 14.7528 - val_acc: 0.0703
Epoch 9/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1330 - acc: 0.9792 - val_loss: 14.7566 - val_acc: 0.0706
Epoch 10/10
31803/31803 [==============================] - 42s 1ms/step - loss: 0.1282 - acc: 0.9801 - val_loss: 14.5013 - val_acc: 0.0703
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[40]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;tensorflow.python.keras._impl.keras.callbacks.History at 0x2d7a6c6f908&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>When divided by 255, we can observe that there is more loss.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Step-3:-Use-the-model-to-solve-CAPTCHAs!">Step 3: Use the model to solve CAPTCHAs!<a class="anchor-link" href="#Step-3:-Use-the-model-to-solve-CAPTCHAs!">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The rest part can be run independently once models are saved.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Get an image from the online demo: <a href="https://contactform7.com/captcha/">https://contactform7.com/captcha/</a> and try our model on it:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[178]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#reading image from local disk</span>
<span class="kn">from</span> <span class="nn">cv2</span> <span class="k">import</span> <span class="n">imread</span>
<span class="n">image</span> <span class="o">=</span> <span class="n">imread</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;C:\Users\Yash\Desktop\image.png&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[178]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.image.AxesImage at 0x2d7a98537b8&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Load saved model data:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[169]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">tensorflow.python.keras.models</span> <span class="k">import</span> <span class="n">load_model</span>
<span class="kn">import</span> <span class="nn">pickle</span>

<span class="n">MODEL_FILENAME</span> <span class="o">=</span> <span class="s2">&quot;captcha_model.hdf5&quot;</span>
<span class="n">MODEL_LABELS_FILENAME</span> <span class="o">=</span> <span class="s2">&quot;model_labels.dat&quot;</span>

<span class="c1"># Load up the model labels (so we can translate model predictions to actual letters)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">MODEL_LABELS_FILENAME</span><span class="p">,</span> <span class="s2">&quot;rb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">lb</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>

<span class="c1"># Load the trained neural network</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">load_model</span><span class="p">(</span><span class="n">MODEL_FILENAME</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Load packages and define functions for independent running of Part 3:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[170]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">imutils</span>
<span class="kn">import</span> <span class="nn">cv2</span>

<span class="c1"># [!!! please also run the cell defining function &quot;resize_to_fit&quot; again, if you run Part 3 alone]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Get the letters from the downloaded images:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[179]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Load the image and convert it to grayscale</span>


<span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2GRAY</span><span class="p">)</span>

<span class="c1"># Add some extra padding around the image</span>
<span class="n">gray</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">copyMakeBorder</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">BORDER_REPLICATE</span><span class="p">)</span>

<span class="c1"># threshold the image (convert it to pure black and white)</span>
<span class="n">thresh</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">threshold</span><span class="p">(</span><span class="n">gray</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_BINARY_INV</span> <span class="o">|</span> <span class="n">cv2</span><span class="o">.</span><span class="n">THRESH_OTSU</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>

<span class="c1"># find the contours (continuous blobs of pixels) the image</span>
<span class="n">contours</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">findContours</span><span class="p">(</span><span class="n">thresh</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="n">cv2</span><span class="o">.</span><span class="n">RETR_EXTERNAL</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">CHAIN_APPROX_SIMPLE</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>

<span class="n">letter_image_regions</span> <span class="o">=</span> <span class="p">[]</span>

<span class="c1"># Now we can loop through each of the four contours and extract the letter</span>
<span class="c1"># inside of each one</span>
<span class="k">for</span> <span class="n">contour</span> <span class="ow">in</span> <span class="n">contours</span><span class="p">:</span>
    <span class="c1"># Get the rectangle that contains the contour</span>
    <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">)</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">boundingRect</span><span class="p">(</span><span class="n">contour</span><span class="p">)</span>
    <span class="n">letter_image_regions</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span>

<span class="c1"># If we found more or less than 4 letters in the captcha, our letter extraction</span>
<span class="c1"># didn&#39;t work correcly. Skip the image instead of saving bad training data!</span>
<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">4</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;[WARNING]&#39;</span><span class="p">,</span> <span class="n">TEST_FILE_NAME</span><span class="p">,</span> <span class="s1">&#39;has&#39;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">),</span> <span class="s1">&#39;contours, unable to process&#39;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;[SUCCESS]&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[SUCCESS]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you see a warning, use another image instead and repeat the previous steps.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Otherwise, continue to create an output image:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[180]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Sort the detected letter images based on the x coordinate to make sure</span>
<span class="c1"># we are processing them from left-to-right so we match the right image</span>
<span class="c1"># with the right letter</span>
<span class="n">letter_image_regions</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">letter_image_regions</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>

<span class="c1"># Create an output image and a list to hold our predicted letters</span>
<span class="n">output</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">merge</span><span class="p">([</span><span class="n">gray</span><span class="p">]</span> <span class="o">*</span> <span class="mi">3</span><span class="p">)</span> <span class="c1"># 2D gray image -&gt; 3D color image</span>

<span class="c1"># show the 3D image</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="c1">#The line above is necesary to show Matplotlib&#39;s plots inside a Jupyter Notebook</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="k">import</span> <span class="n">pyplot</span> <span class="k">as</span> <span class="n">plt</span>

<span class="c1">#Show the image with matplotlib</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
+27J7kv6Vlf7QmpqatKUnOSlEb2ISOCKCnozO9HMnjCzd8xsp5n9s5kNMbMXzGx3dD6463sSEZFy
KXZEvxx4zt3PAM4FdgKLgA3uPg7YEF0XEZGY9DrozeyzwBeBlQDu/ld3/yMwDVgVrbYKmF5skSIi
0nvFjOjHAG3AQ2b2upk9YGYDgJPd/SBAdK6jXUhZNDc309zczJAhQzCzo05VVVW89tprHb8dEPk0
KyboK4AJwH3ufh5wmB5M05hZrZk1mFlDW1tbEWWIiEghxQT9AeCAu78aXX+CdPC/b2bDAKLz1lw3
dvc6d6929+qhQ4cWUYaIiBTS66B3998B+83s9KhpMvAbYD1QE7XVAOuKqlA+Nfbu3cvhw4e7ffCJ
lpYWWlpaitrLp8inQbE/mPo34GEzOwFoBq4n/c/j52Y2B9gHfL3IxxARkSIUFfTu/gZQnWPR5GLu
Vz7x1ltvxV1CSZ111ll5l+3atatjNN+dHXTt2rUr77L+/fszatSoHtcnEiLtAiFmFRXpl2DcuHE5
l+/duxdIH0uzq/Dbt28f8MkeADs7/fTTc7b3pfHjx+dddujQITZs2ADAzJkzC95PKpXiqaeeKvg4
Sdybo0gctAsEEZHAaUSfEPmmNLZt2wbA3XffXfDgEoUOXJI5qPTYsWNLUGlxModJPPXUUzs+gWSr
ra0F0jtzKzTNU19fX/DA6VdeeWVQI/qGhoac/SXSHRrRi4gETiP6hLj22mtZunQpQM6R29KlS3nv
vfcA+OY3v8no0aMBePHFFwF44IEH2Lp1a877njp1KpCMI0tVVVUBsHjxYubMmXPM8kOHDgFw/vnn
d/TH1Vdf3dEnd911FwDPP/98zvvPHJHrxhtvLG3hZdDY2NjlOpnXN3OYyM4yz3fyZG3/IPkp6BOi
qqqKhx9+GMh/GLX6+vqjzrujsrKSRYuSt1+5WbNmdXyZmmsKpr29vaPuntRfV1cH0K0DtcQlc5CZ
fAeb6Yn58+cDyX6+Ej9N3YiIBE4j+gS56KKLAHjuueeA9CaGvf3VZ+bIVI888kjBLzXjUlFR0XHQ
6MyodMWKFb26r8rKSjZu3AgkY3qqL8yePRug4Bf0IhkK+gS67LLLAGhtbeWBBx4AYPXq1WzevDnv
bSorK5k0aRIA8+bNY/r05O8dOvMbguXLlwOwYMEC7rnnHgB+9atf5f3OAeCCCy7ghhtuAGDGjBlB
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
UwI3/AAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[181]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="p">[]</span>

<span class="c1"># Save out each letter as a single image</span>
<span class="k">for</span> <span class="n">letter_bounding_box</span> <span class="ow">in</span> <span class="n">letter_image_regions</span><span class="p">:</span>
    <span class="c1"># Grab the coordinates of the letter in the image</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="n">letter_bounding_box</span>

    <span class="c1"># Extract the letter from the original image with a 2-pixel margin around the edge</span>
    <span class="n">letter_image</span> <span class="o">=</span> <span class="n">gray</span><span class="p">[</span><span class="n">y</span> <span class="o">-</span> <span class="mi">2</span><span class="p">:</span><span class="n">y</span> <span class="o">+</span> <span class="n">h</span> <span class="o">+</span> <span class="mi">2</span><span class="p">,</span> <span class="n">x</span> <span class="o">-</span> <span class="mi">2</span><span class="p">:</span><span class="n">x</span> <span class="o">+</span> <span class="n">w</span> <span class="o">+</span> <span class="mi">2</span><span class="p">]</span>

    <span class="c1"># Re-size the letter image to 20x20 pixels to match training data</span>
    <span class="n">letter_image</span> <span class="o">=</span> <span class="n">resize_to_fit</span><span class="p">(</span><span class="n">letter_image</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>
    
    <span class="c1"># Turn the single image into a 4D list of images to make Keras happy</span>
    <span class="c1"># 4D: image_number (=1) x height x width x channel (=1)</span>
    <span class="n">letter_image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">expand_dims</span><span class="p">(</span><span class="n">letter_image</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">letter_image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">expand_dims</span><span class="p">(</span><span class="n">letter_image</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
    
    <span class="c1"># Ask the neural network to make a prediction</span>
    <span class="n">prediction</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">letter_image</span><span class="p">)</span> <span class="c1"># output is one-hot encoded</span>
        
    <span class="n">letter</span> <span class="o">=</span> <span class="n">lb</span><span class="o">.</span><span class="n">inverse_transform</span><span class="p">(</span><span class="n">prediction</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="c1"># use [0] since there is only one test data&#39;s label item in the list</span>
    <span class="n">predictions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">letter</span><span class="p">)</span>
    
    <span class="c1"># draw the prediction on the output image</span>
    <span class="c1"># (255, 0, 0) = red</span>
    <span class="n">cv2</span><span class="o">.</span><span class="n">rectangle</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="n">y</span> <span class="o">-</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">w</span> <span class="o">+</span> <span class="mi">4</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">h</span> <span class="o">+</span> <span class="mi">4</span><span class="p">),</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">cv2</span><span class="o">.</span><span class="n">putText</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="n">letter</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">-</span> <span class="mi">8</span><span class="p">),</span> <span class="n">cv2</span><span class="o">.</span><span class="n">FONT_HERSHEY_SIMPLEX</span><span class="p">,</span> <span class="mf">0.55</span><span class="p">,</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>

<span class="c1"># see prediction result:</span>

<span class="c1"># Print the captcha&#39;s text</span>
<span class="n">captcha_text</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">predictions</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;CAPTCHA text is: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">captcha_text</span><span class="p">))</span>

<span class="c1"># Show the annotated image</span>
<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>CAPTCHA text is: 8CHH
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
OCV6EZHA/T9550H51FkbYQAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Questions: Is the prediction correct? How many letters are correctly predicted?</p>
<p><strong>Type Your Answer Here:</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It's not predicted correctly.Three letters are predicted correctly.</p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
