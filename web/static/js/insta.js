$(function() {
	var access_token = location.hash.split('=')[1];
		  
	$.ajax({
    	type: "GET",
        dataType: "jsonp",
        cache: false,
        url: "https://api.instagram.com/v1/tags/littletinker/media/recent?access_token=9765868.e50f97d.ccdba76c976a4e69b01beeee68947305",
        success: function(data) {

            for (var i = 0; i < 40; i++) {
        $("#instafeed").append("<div class='instaframe'><a target='_blank' href='" + data.data[i].link +"'><img src='" + data.data[i].images.low_resolution.url +"' /></a></div>");   
      		}     
                            
        }
    });	
});
	
