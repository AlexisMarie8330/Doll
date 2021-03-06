Rails.application.routes.draw do
  get 'articles/index'

  get 'barbie/family'

  get 'barbie/hotel'

  get 'barbie/thanksgiving'

  get 'barbie/party'

  get 'barbie/filipina'

  get 'interview/pamela'

  get 'interview/Pamela'

  get 'barbie/dollhouses'

  get 'barbie/playsets'

  get 'barbie/giftguide'

  get 'barbie/cars'

  get 'barbie/dresses'

  get 'barbie/lingerie'

  get 'etsy/wishlist2'

  get 'etsy/wishlist'

  get 'miniatures/instagram'

  get 'interview/nadine'

  get 'interview/Nadine'

  get 'welcome/nadine'

  get 'welcome/blythedresses'

  get 'welcome/ads'

  get 'welcome/fashion'

  get 'welcome/index'

  get 'welcome/lingerie'

  get 'welcome/cars'

  get 'welcome/pop'

  get 'welcome/Pop-Culture'

  get 'welcome/instagram'

  get 'welcome/index'

  get 'welcome/post'

  get 'welcome/index'

  get 'feed.rss', to: 'feeds#rss', :format => 'rss'

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
