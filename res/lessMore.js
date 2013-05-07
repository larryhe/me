function hookLessMore(){
     var adjustheight = 240,
     // The "more" link text
         moreText = '... More',
         lessText = 'Less',
         moreLess = '<span class="moreLess">' + moreText + '</span>';
     //generate more icon if necessary
     $('div.article p.content').each(function(){
         var content = $(this);
         if(content.prop('scrollHeight') > adjustheight){
             //append more icon
            content.parent().append(moreLess);
         }
     });
     $(".moreLess").on('click',function() {
         var content = $(this).parent().find("p.content");
         if($(this).text() == moreText){
            content.animate({height: content.prop('scrollHeight'),overflow: 'visible'}, 500);
            $(this).text(lessText); 
         }else{
            content.animate({height: adjustheight, overflow: 'hidden'}, 500);
            $(this).text(moreText);
         }
     });
}
