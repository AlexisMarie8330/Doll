require 'test_helper'

class BarbieControllerTest < ActionController::TestCase
  test "should get dollhouses" do
    get :dollhouses
    assert_response :success
  end

end
