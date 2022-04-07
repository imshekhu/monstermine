# monstermine

Project aims at enabling non technical people to create mines of crypto currency and monitor their Hashrate and payouts.

* Backend : 
  * Stack - Python, Heroku, Django, Postgres
  * DB Tables - Auth_user (id, email, first_name, last_name, password, phone, payoutaddress, amountmined, amountachieved, currentcoin, minespeed, minerconnected, nextpayout, watcherlink, binance_profile_token, profit_today, profit_yesterday)
  * WORKFLOW - 
    *  User logs in into the server.
    *  HomeView : Return Account Data by fetching binance watcher link stored inside db by Admin
      * get - user requests.get and ping binance to fetch the earning using binance profile token.
      * post - Save any changes made to profile.
* Worker :
  * configured binance pool and create a new worker.
  * add config from worker to local bminer.
  * bminer ping the server.

** OC settings - 
  * 1660 Super - -200(core), +900(mem)
  * 3060 - (470 dev drivers) -300(core), +1307(mem)
