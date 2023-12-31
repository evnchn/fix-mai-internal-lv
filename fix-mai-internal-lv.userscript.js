// ==UserScript==
// @name         fix-mai-internal-lv
// @namespace    https://github.com/evnchn/fix-mai-internal-lv
// @version      0.2
// @description  mai-tools broke because maidx_in_lv_festivalplus.js no longer available from upstream data source. This is a hotfix to put in the "magicVer20" required for function.
// @match        https://maimaidx-eng.com/maimai-mobile/record/*
// @match        https://myjian.github.io/mai-tools/rating-calculator/*
// @downloadURL  https://raw.githubusercontent.com/evnchn/fix-mai-internal-lv/main/fix-mai-internal-lv.userscript.js
// @updateURL    https://raw.githubusercontent.com/evnchn/fix-mai-internal-lv/main/fix-mai-internal-lv.userscript.js
// ==/UserScript==

// V0.1: emergency release

// V0.2: include myjian.github.io domain

(function () {
    'use strict';

    function fetchCustomData() {
        const magicVer20 = localStorage.getItem('magicVer20');
        const magicExpire = localStorage.getItem('magicExpire');
        const currentMsTime = new Date().getTime();
        const customUrl = 'https://raw.githubusercontent.com/evnchn/fix-mai-internal-lv/main/testing/detail.str'; // Replace with your custom URL
        fetch(customUrl)
            .then((customResponse) => customResponse.text())
            .then((customData) => {
                localStorage.setItem('magicVer20', customData);
                const expiryTime = currentMsTime + 3600000; // 1 hour in milliseconds
                localStorage.setItem('magicExpire', Math.floor(expiryTime / 1));
                alert("LOADED! works for an hour...")
            })
            .catch((error) => {
                console.error('Error fetching from custom_url:', error);
            });

    }
    if (location.href.indexOf("myjian") != -1) {
        var button = document.createElement("button");
        button.innerHTML = "HOTFIX mai-tools";
        button.addEventListener("click", fetchCustomData);
        document.body.prepend(button);
    } else {
        document.querySelector("header").nextElementSibling.querySelectorAll('img.w_120')[3].style.filter = "invert()"
        document.querySelector("header").nextElementSibling.querySelectorAll('img.w_120')[3].onclick = function () { fetchCustomData() }
    }

})();