
## fallback
- utter_default

## greeting path 1
* greet
- utter_greet

## fine path 1
* hoi_ten
- utter_ten

## ask path 1
* hoi_id
- utter_awsid

## fine path 2
* fine_normal
- utter_help

## fine path 3
* fine_ask
- utter_reply

## news path 1
* san_pham
- utter_ofc
- action_get_news

## news path 2
* san_pham_num
- utter_ofc_n
- action_get_num

## news path 3
* find_id
- utter_id
- action_get_id

## stories path 1
* greet
- utter_greet
* hoi_ten
- utter_ten
* fine_normal
- utter_help
* bye
- utter_bye

## stories path 2
* hoi_ten
- utter_ten
* fine_ask
- utter_reply
* fine_normal
- utter_help
* san_pham
- utter_ofc
- action_get_news
* cam_on
- utter_repfun
* bye
- utter_bye

## stories path 3
* greet
- utter_greet
* find_id
- utter_id
- action_get_id
* cam_on
- utter_repfun
* bye
- utter_bye

## stories path 4
* greet
- utter_greet
* san_pham_num
- utter_ofc_n
- action_get_num
* hoi_id
- utter_awsid
* find_id
- utter_id
- action_get_id
* bye
- utter_bye

## stories path 5
* fine_ask
- utter_reply
* san_pham_num
- utter_ofc_n
- action_get_num

## stories path 6 
* greet
- utter_greet
* hoi_ten
- utter_ten
* fine_ask
- utter_reply
* fine_normal
- utter_help
* san_pham_num
- utter_ofc_n
- action_get_num
* find_id
- utter_id
- action_get_id
* cam_on
- utter_repfun

##  stories path 7
* greet
- utter_greet
* hoi_ten
- utter_ten
* fine_normal
- utter_help
* san_pham
- utter_ofc
- action_get_news
* san_pham_num
- utter_ofc_n
- action_get_num
* hoi_id
- utter_awsid
* find_id
- utter_id
- action_get_id
* cam_on
- utter_repfun
* bye
- utter_bye

## thanks path 1
* cam_on
- utter_repfun

## bye path 1
* bye
- utter_bye