
/*
	* haylep-JS ~ 
	* :: Now with support for touch events and multiple instances for 
	* :: those situations that call for multiple easter eggs!
	* Code: http://haylep-js.googlecode.com/
	* Examples: http://www.snaptortoise.com/haylep-js
	* Copyright (c) 2009 George Mandis (georgemandis.com, snaptortoise.com)
	* Version: 1.3.3 (4/16/2011)
	* Licensed under the GNU General Public License v3
	* http://www.gnu.org/copyleft/gpl.html
	* Tested in: Safari 4+, Google Chrome 4+, Firefox 3+, IE7+, Mobile Safari 2.2.1 and Dolphin Browser
*/

var haylep = function() {
	var haylep= {
			addEvent:function ( obj, type, fn, ref_obj )
			{
				if (obj.addEventListener)
					obj.addEventListener( type, fn, false );
				else if (obj.attachEvent)
				{
					// IE
					obj["e"+type+fn] = fn;
					obj[type+fn] = function() { obj["e"+type+fn]( window.event,ref_obj ); }
	
					obj.attachEvent( "on"+type, obj[type+fn] );
				}
			},
	        input:"",
	        pattern:"3838404037393739666513",
		/*pattern:"38384040373937396665",*/
	        load: function(link) {					
				this.addEvent(document,"keydown", function(e,ref_obj) {											
					if (ref_obj) haylep = ref_obj; // IE
					haylep.input+= e ? e.keyCode : event.keyCode;
					if (haylep.input.length > haylep.pattern.length) haylep.input = haylep.input.substr((haylep.input.length - haylep.pattern.length));
					if (haylep.input == haylep.pattern) {
                    haylep.code(link);
					haylep.input="";
                   	return;
                    }
            	},this);
           this.iphone.load(link)
	                
				},
	        code: function(link) { window.location=link},
	        iphone:{
	                start_x:0,
	                start_y:0,
	                stop_x:0,
	                stop_y:0,
	                tap:false,
	                capture:false,
					orig_keys:"",
	                keys:["UP","UP","DOWN","DOWN","LEFT","RIGHT","LEFT","RIGHT","TAP","TAP","TAP"],
	                code: function(link) { haylep.code(link);},
	                load: function(link){
									this.orig_keys = this.keys;
	    							haylep.addEvent(document,"touchmove",function(e){
	                          if(e.touches.length == 1 && haylep.iphone.capture==true){ 
	                            var touch = e.touches[0]; 
	                                haylep.iphone.stop_x = touch.pageX;
	                                haylep.iphone.stop_y = touch.pageY;
	                                haylep.iphone.tap = false; 
	                                haylep.iphone.capture=false;
	                                haylep.iphone.check_direction();
	                                }
	                                });               
	                        haylep.addEvent(document,"touchend",function(evt){
	                                if (haylep.iphone.tap==true) haylep.iphone.check_direction(link);           
	                                },false);
	                        haylep.addEvent(document,"touchstart", function(evt){
	                                haylep.iphone.start_x = evt.changedTouches[0].pageX
	                                haylep.iphone.start_y = evt.changedTouches[0].pageY
	                                haylep.iphone.tap = true
	                                haylep.iphone.capture = true
	                                });               
	                                },
	                check_direction: function(link){
	                        x_magnitude = Math.abs(this.start_x-this.stop_x)
	                        y_magnitude = Math.abs(this.start_y-this.stop_y)
	                        x = ((this.start_x-this.stop_x) < 0) ? "RIGHT" : "LEFT";
	                        y = ((this.start_y-this.stop_y) < 0) ? "DOWN" : "UP";
	                        result = (x_magnitude > y_magnitude) ? x : y;
	                        result = (this.tap==true) ? "TAP" : result;                     

	                        if (result==this.keys[0]) this.keys = this.keys.slice(1,this.keys.length)
	                        if (this.keys.length==0) { 
														this.keys=this.orig_keys;
														this.code(link)
														}
	                        }
	                }
	}
	return haylep;
}