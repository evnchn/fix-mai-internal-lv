# fix-mai-internal-lv
mai-tools broke because maidx_in_lv_festivalplus.js no longer available from upstream data source. This is a hotfix to regenerate said file.

## Actual hot-fix usable by user

Add this to bookmarklet

`javascript:(function()%7Bconst%20magicVer20%3DlocalStorage.getItem(%22magicVer20%22)%2CmagicExpire%3DlocalStorage.getItem(%22magicExpire%22)%2CcurrentMsTime%3Dnew%20Date().getTime()%2CcustomUrl%3D%22https%3A%2F%2Fraw.githubusercontent.com%2Fevnchn%2Ffix-mai-internal-lv%2Fmain%2Ftesting%2Fdetail.str%22%3Bfetch(%22https%3A%2F%2Fraw.githubusercontent.com%2Fevnchn%2Ffix-mai-internal-lv%2Fmain%2Ftesting%2Fdetail.str%22).then(t%3D%3Et.text()).then(t%3D%3E%7BlocalStorage.setItem(%22magicVer20%22%2Ct)%3Blet%20e%3DcurrentMsTime%2B36e5%3BlocalStorage.setItem(%22magicExpire%22%2CMath.floor(e%2F1))%2Calert(%22LOADED!%20works%20for%20an%20hour...%22)%7D).catch(t%3D%3E%7Bconsole.error(%22Error%20fetching%20from%20custom_url%3A%22%2Ct)%7D)%3B%7D)()%3B`

or add `fix-mai-internal-lv.userscript.js` as userscript, then press the inverted button 

<img width="412" alt="image" src="https://github.com/evnchn/fix-mai-internal-lv/assets/37951241/d07b39cc-b611-4299-a97c-2d1db595258b">


## How to test this internal level database before mai-tools officially use it

1. Edit the hosts file at `C:\Windows\System32\drivers\etc` and add entry `127.0.0.1 sgimera.github.io` to point the upstream data source domain to localhost
2. Go to `chrome://net-internals/#hsts` to clear HSTS for `sgimera.github.io`
3. Place `localhost.pem` in the testing folder by going to https://regery.com/en/security/ssl-tools/self-signed-certificate-generator and copying both the private key and public key text to `localhost.pem`
4. Run `server.py`
5. Visit https://sgimera.github.io/mai_RatingAnalyzer/scripts_maimai/maidx_in_lv_festivalplus.js and press OK on all the security errors \(you caused them yourselves\)
6. Enjoy your internal levels!
