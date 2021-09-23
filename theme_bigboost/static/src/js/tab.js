odoo.define('theme_bigboost.tab', function(require) {"use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');


    $(document).ready(function(){

        // SHOP Product SORTING Update
        $("#sorting_shop").change(function(){
            var sorting_shop =  $("#sorting_shop").val()
            if(sorting_shop){
                 window.location = sorting_shop
            }
        })

        // SHOP Product PPG Update
        $("#ppg_shop").change(function(){
            var ppg_shop =  $("#ppg_shop").val()
            if(ppg_shop){
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

        // Product Timer JS
         if($('#timer').length>0){
        var date = $('#timer').val()
        if(date != "nan")
        {
          var countDownDate = new Date(date).getTime();
          var countDownDate = new Date(countDownDate - 330*60000);

          var x = setInterval(function() {

                // Get todays date and time
                var now = new Date().getTime();

                // Find the distance between now an the count down date
                var distance = countDownDate - now;// Time calculations for days, hours, minutes and seconds

                if (distance > 0) {
                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                        if ((seconds+'').length == 1) {
                            seconds = "0" + seconds;
                        }
                        if ((days+'').length == 1) {
                            days = "0" + days;
                        }
                        if ((hours+'').length == 1) {
                            hours = "0" + hours;
                        }
                        if ((minutes+'').length == 1) {
                            minutes = "0" + minutes;
                        }
                }
                // If the count down is over, write some text
                if (distance <= 0)
                {
                    clearInterval(x);
                    seconds = "00" ;
                    days = "00";
                    minutes = "00";
                    hours = "00";
                    $('.js_timer_div').empty();
                }
                $('#second').html(seconds)
                $('#minite').html(minutes)
                $('#hour').html(hours)
                $('#day').html(days)
                }, 1000);
        }
    }

        // Add to cart for product page
        $("#add_to_cart_custom").click(function(){
            console.log("======CART MA ADD KARVANU CHHE========")
            var product_template_id = $(this).closest("form").find(".product_id").val()
            var add_qty = $(this).closest("form").find(".quantity").val()
            console.log("======CART MA ADD KARVANU CHHE======product_template_id==",product_template_id)
            console.log("======CART MA ADD KARVANU CHHE======product_template_id==",add_qty)

            if(product_template_id && add_qty){
                ajax.jsonRpc('/custom_cart', 'call', {'product_template_id': product_template_id, 'add_qty':add_qty}).then(function(data){
                  if(data){
                    $('#addtocart').modal('show');
                  }
                })
            }
         })

        // Add to cart for shop page
        $(".add_to_cart_custom").click(function(){
            var elmId = $(this).attr("id");
            if(elmId){
                var product_template_id = $(this).closest("form").find(".product_id").val()
                var add_qty = 1
                if(product_template_id && add_qty){
                    ajax.jsonRpc('/custom_cart', 'call', {'product_template_id': product_template_id, 'add_qty':add_qty}).then(function(data){
                      if(data){
                        $('#addtocart-'+elmId).modal('show');
                      }
                    })
                }
            }
         })

    });

});