class FeedsController < ApplicationController
 
  layout false
 
  def rss
    @posts = Post.published_posts.limit(50)
  end
 
end