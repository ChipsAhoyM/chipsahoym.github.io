// Citation counts from the Semantic Scholar API.
// Runs only on pages that render publication entries (.cited-by elements).
// Results are cached in localStorage for 14 days; failures hide the badge.
(function () {
  'use strict';

  function cacheGet(key) {
    try {
      var item = JSON.parse(localStorage.getItem(key));
      if (item && Date.now() - item.ts < 14 * 24 * 3600 * 1000) return item;
    } catch (e) { /* ignore */ }
    return null;
  }

  function cacheSet(key, value) {
    try { localStorage.setItem(key, JSON.stringify({ ts: Date.now(), value: value })); }
    catch (e) { /* ignore */ }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var badges = Array.prototype.slice.call(document.querySelectorAll('.cited-by'));
    if (!badges.length) return;

    var delay = 1100; // Semantic Scholar unauthenticated rate limit is shared; be polite.

    badges.forEach(function (badge, i) {
      var title = badge.getAttribute('data-title');
      if (!title) return;
      // strip LaTeX tokens so the query matches the plain title
      title = title.replace(/\$[^$]*\$/g, ' ').replace(/\\[a-zA-Z]+/g, ' ')
                   .replace(/[{}\^_~]/g, '').replace(/\s+/g, ' ').trim();
      var cacheKey = 's2-citation:' + title;

      setTimeout(function () {
        var cached = cacheGet(cacheKey);
        if (cached) { fill(badge, cached); return; }

        var url = 'https://api.semanticscholar.org/graph/v1/paper/search/match'
          + '?query=' + encodeURIComponent(title)
          + '&fields=citationCount,url';
        fetch(url)
          .then(function (r) {
            if (!r.ok) throw new Error('S2 status ' + r.status);
            return r.json();
          })
          .then(function (data) {
            var item = data && Array.isArray(data.data) ? data.data[0] : (data && data.data);
            if (!item) throw new Error('S2 no match');
            var value = { count: item.citationCount || 0, url: item.url };
            cacheSet(cacheKey, value);
            fill(badge, value);
          })
          .catch(function () { /* badge stays hidden */ });
      }, i * delay);
    });

    function fill(badge, value) {
      badge.textContent = 'cited by ' + value.count;
      badge.href = value.url || '#';
      badge.style.display = '';
    }
  });
})();
