require 'test_helper'

class BlogControllerTest < ActionController::TestCase
  test "should get Nadine" do
    get :Nadine
    assert_response :success
  end

end
