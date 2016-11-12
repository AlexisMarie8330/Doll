require 'test_helper'

class BarbieControllerTest < ActionController::TestCase
  test "should get lingerie" do
    get :lingerie
    assert_response :success
  end

end
