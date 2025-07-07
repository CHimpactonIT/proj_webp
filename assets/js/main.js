
(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }})


function showMetadataTab(tab, btn) {
  // Tab highlight
  document.querySelectorAll('.btn-metadata-tab').forEach(b => b.classList.remove('btn-metadata-active', 'active'));
  if (btn) btn.classList.add('btn-metadata-active', 'active');

  // Hide all
  document.getElementById('metadata-cat').style.display = 'none';
  document.getElementById('metadata-ds1').style.display = 'none';
  document.getElementById('metadata-ds2').style.display = 'none';
  document.getElementById('metadata-ds3').style.display = 'none';
  document.getElementById('metadata-ds4').style.display = 'none';
  document.getElementById('metadata-ds5').style.display = 'none';
  document.getElementById('metadata-ds6').style.display = 'none';
  document.getElementById('metadata-ds7').style.display = 'none';
  document.getElementById('metadata-ds8').style.display = 'none';
  document.getElementById('metadata-ds9').style.display = 'none';
  document.getElementById('metadata-ds10').style.display = 'none';

  // Show selected
  if (tab === 'catalog') {
    document.getElementById('metadata-cat').style.display = 'block';
  } else if (tab === 'ds1') {
    document.getElementById('metadata-ds1').style.display = 'block';
  } else if (tab === 'ds2') {
    document.getElementById('metadata-ds2').style.display = 'block';
  } else if (tab === 'ds3') {
    document.getElementById('metadata-ds3').style.display = 'block';
  } else if (tab === 'ds4') {
    document.getElementById('metadata-ds4').style.display = 'block';
  } else if (tab === 'ds5') {
    document.getElementById('metadata-ds5').style.display = 'block';
  } else if (tab === 'ds6') {
    document.getElementById('metadata-ds6').style.display = 'block';
  } else if (tab === 'ds7') {
    document.getElementById('metadata-ds7').style.display = 'block';
  } else if (tab === 'ds8') {
    document.getElementById('metadata-ds8').style.display = 'block';
  } else if (tab === 'ds9') {
    document.getElementById('metadata-ds9').style.display = 'block';
  } else if (tab === 'ds10') {
    document.getElementById('metadata-ds10').style.display = 'block';
  }

}

function showMashupViz(id, btn) {
  document.querySelectorAll('.mashup-viz-container').forEach(el => el.style.display = 'none');
  document.getElementById(id).style.display = 'block';
  document.querySelectorAll('.btn-mashup').forEach(b => b.classList.remove('btn-mashup-active', 'active'));
  btn.classList.add('btn-mashup-active', 'active');

  if (id === 'mashup1-container') {
    showMashup1Tab('tab1', document.querySelector('.btn-mashup1-tab'));
  } else if (id === 'mashup2-container') {
    showMashup2Tab("tab6", document.querySelector('.btn-mashup2-tab'));
  }
}


function showMashup1Tab(tab, btn) {
  // Tab highlight
  document.querySelectorAll('.btn-mashup1-tab').forEach(b => b.classList.remove('btn-mashup-active', 'active'));
  if (btn) btn.classList.add('btn-mashup-active', 'active');

  // Hide all
  document.getElementById('mashup1-fig1').style.display = 'none';
  document.getElementById('mashup1-fig2').style.display = 'none';
  document.getElementById('mashup1-fig3').style.display = 'none';
  document.getElementById('mashup1-fig4').style.display = 'none';
  document.getElementById('mashup1-fig5').style.display = 'none';

  // Show selected
  if (tab === 'tab1') {
    document.getElementById('mashup1-fig1').style.display = 'block';
  } else if (tab === 'tab2') {
    document.getElementById('mashup1-fig2').style.display = 'block';
  } else if (tab === 'tab3') {
    document.getElementById('mashup1-fig3').style.display = 'block';
  }
  else if (tab === 'tab4') {
    document.getElementById('mashup1-fig4').style.display = 'block';
  }
  else if (tab === 'tab5') {
    document.getElementById('mashup1-fig5').style.display = 'block';
  }
}

function showMashup2Tab(tab, btn) {
  // Tab highlight
  document.querySelectorAll('.btn-mashup2-tab').forEach(b => b.classList.remove('btn-mashup-active', 'active'));
  if (btn) btn.classList.add('btn-mashup-active', 'active');

  // Hide all
  document.getElementById('mashup2-fig1').style.display = 'none';
  document.getElementById('mashup2-fig2').style.display = 'none';
  document.getElementById('mashup2-fig3').style.display = 'none';
  document.getElementById('mashup2-fig4').style.display = 'none';

  // Show selected
  if (tab === 'tab6') {
    document.getElementById('mashup2-fig1').style.display = 'block';
  } else if (tab === 'tab7') {
    document.getElementById('mashup2-fig2').style.display = 'block';
  } else if (tab === 'tab8') {
    document.getElementById('mashup2-fig3').style.display = 'block';
  }
  else if (tab === 'tab9') {
    document.getElementById('mashup2-fig4').style.display = 'block';
  }
}