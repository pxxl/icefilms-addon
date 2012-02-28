#!/usr/bin/env python

# Links and info about metacontainers.
# Update this file to update the containers.

# Size is in MB

#return dictionary of strings and integers
def get():
          containers = {} 

          #date updated
          containers['date'] = 'March 2012'
          
          #--- Database Meta Container ---# 
          containers['db_url'] = 'http://minus.com/mhRcwPnWX'
          containers['db_filename'] = 'video_cache.zip'
          containers['db_size'] = 2
                    
          #--- Movie Meta Container ---# 

          #basic container        
          containers['mv_covers_url'] = 'http://minus.com/mhRcwPnWX'
          containers['mv_covers_filename'] = 'movie_covers.zip'
          containers['mv_cover_size'] = 53
          
          containers['mv_backdrop_url'] = 'http://minus.com/mhRcwPnWX'
          containers['mv_backdrop_filename'] = 'movie_backdrops.zip'
          containers['mv_backdrop_size'] = 735
          
          #--- TV   Meta  Container ---#

          #basic container       
          containers['tv_covers_url'] = 'http://minus.com/mhRcwPnWX'
          containers['tv_covers_filename'] = 'tv_covers.zip'
          containers['tv_cover_size'] = 131

          containers['tv_banners_url'] = 'http://minus.com/mhRcwPnWX'
          containers['tv_banners_filename'] = 'tv_banners.zip'
          containers['tv_banners_size'] = 45


          containers['tv_backdrop_url'] = 'http://minus.com/mhRcwPnWX'
          containers['tv_backdrop_filename'] = 'tv_backdrops.zip'
          containers['tv_backdrop_size'] = 210
          
          
          #additional container
          containers['tv_add_url'] = ''
          containers['tv_add_size'] = 0       


          return containers
