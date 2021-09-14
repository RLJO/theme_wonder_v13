odoo.define('theme_bigboost.tab', function(require) {"use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');


    $(document).ready(function(){

        $("#sorting_shop").change(function(){
            var sorting_shop =  $("#sorting_shop").val()
            if(sorting_shop){
                 window.location = sorting_shop
            }
        })

        $("#ppg_shop").change(function(){
            var ppg_shop =  $("#ppg_shop").val()
            console.log("=========ppg_shop===========",ppg_shop)
            if(ppg_shop){
                 console.log("=========RPC CALL===========",ppg_shop)
                 if(ppg_shop){
                    rpc.query({route: '/ppg_shop/update',
                        params:{
                            ppg_shop:ppg_shop,
                        }
                    }).then(function (result) {
                        if(result){
                            window.location.reload();
                        }
                    })
                 }
            }
        })

    });

});