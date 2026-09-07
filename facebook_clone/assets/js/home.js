(function(){
      const profileImg = document.querySelector('.nav-right .profile-image');
      const profileAnchor = profileImg ? profileImg.closest('a') : null;
      const profilePopup = document.getElementById('profilePopup');

      function togglePopup(e){
        e.preventDefault();
        if(!profilePopup) return;
        profilePopup.classList.toggle('visible');
        profilePopup.setAttribute('aria-hidden', String(!profilePopup.classList.contains('visible')));
      }

      function hidePopup(){
        if(profilePopup && profilePopup.classList.contains('visible')){
          profilePopup.classList.remove('visible');
          profilePopup.setAttribute('aria-hidden', 'true');
        }
      }

      if(profileAnchor) profileAnchor.addEventListener('click', togglePopup);

      document.addEventListener('click', function(e){
        const target = e.target;
        if(!profilePopup) return;
        if(profileAnchor && (profileAnchor.contains(target) || profilePopup.contains(target))) return;
        hidePopup();
      });

      document.addEventListener('keydown', function(e){
        if(e.key === 'Escape') hidePopup();
      });
    })();
