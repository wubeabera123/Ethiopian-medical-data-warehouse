
  
    

  create  table "data_warehouse"."public"."my_model__dbt_tmp"
  
  
    as
  
  (
    SELECT 
    sender_id,
    message_id,
    message_text,
    channel,
    date
FROM scraped_data
  );
  