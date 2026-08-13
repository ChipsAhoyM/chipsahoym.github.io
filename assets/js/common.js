// Shared interactions (vanilla JS, no jQuery).
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a.bibtex').forEach(function(link) {
    link.addEventListener('click', function() {
      var entry = link.closest('.pub-content');
      var bibtex = entry ? entry.querySelector('.bibtex.hidden') : null;
      if (bibtex) bibtex.classList.toggle('open');
    });
  });
});
