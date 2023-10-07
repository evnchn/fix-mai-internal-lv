# fix-mai-internal-lv
mai-tools broke because maidx_in_lv_festivalplus.js no longer available from upstream data source. This is a hotfix to regenerate said file.

## How to test this internal level database before mai-tools officially use it

1. Edit the hosts file at `C:\Windows\System32\drivers\etc` and add entry `127.0.0.1 sgimera.github.io` to point the upstream data source domain to localhost
2. Go to `chrome://net-internals/#hsts` to clear HSTS for `sgimera.github.io`
3. Place `localhost.pem` in the testing folder by going to https://regery.com/en/security/ssl-tools/self-signed-certificate-generator and copying both the private key and public key text to `localhost.pem`
4. Run `server.py`
5. Visit https://sgimera.github.io/mai_RatingAnalyzer/scripts_maimai/maidx_in_lv_festivalplus.js and press OK on all the security errors \(you caused them yourselves\)
6. Enjoy your internal levels!
