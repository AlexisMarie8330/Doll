require 'test_helper'

class InterviewControllerTest < ActionController::TestCase
  test "should get nadine" do
    get :nadine
    assert_response :success
  end

end
