require 'test_helper'

class EtsyControllerTest < ActionController::TestCase
  test "should get wishlist" do
    get :wishlist
    assert_response :success
  end

end
