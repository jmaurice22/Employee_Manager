/* Todo: style the leave form using javascript when the window loads.  */

window.onload = function () {
let startdateEL =  document.getElementById('id_start_date');
let enddateEL = document.getElementById('id_end_date');
startdateEL.addEventListener("click", ()=> {
    $(function() {
                $( "#id_start_date" ).datepicker();
                $( "#id_start_date" ).datepicker.show();
            });
})

enddateEL.addEventListener("click", ()=> {
    $(function() {
                $( "#id_end_date" ).datepicker();
                $( "#id_end_date" ).datepicker.show();
            });
})

}

