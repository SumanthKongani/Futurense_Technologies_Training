create database ytb;
use ytb;

show tables;

select * from category_title;
select * from usvideos;

ALTER TABLE usvideos 
ADD FOREIGN KEY (category_id) REFERENCES category_title(category_id);

select * from usvideos a left join  category_title b on a.category_id = b.category_id;
select * from usvideos a left join  category_title b on a.category_id = b.category_id where channel_title = 'MLB';

DELETE FROM usvideos WHERE category_id = 0;

#●	Top 3 videos for which user interaction (views + likes + dislikes + comments) is the highest.

select * from(
select a.*, rank() over (order by user_interaction desc) rnk from(
select  video_id, title, channel_title, max(views+likes+dislikes+comment_count) user_interaction 
from usvideos group by title) a )a where rnk<=3;

#●	Bottom 3 videos for which user interaction (views + likes + dislikes + comments) is lowest.

#when last seen in trening
select * from(
select a.*, rank() over (order by user_interaction) rnk from(
select video_id, title, channel_title, max(views+likes+dislikes+comment_count) user_interaction 
from usvideos group by title) a )a where rnk<=3;

#when first got into trending
select * from(
select a.*, rank() over (order by user_interaction) rnk from(
select video_id, title, channel_title, min(views+likes+dislikes+comment_count) user_interaction 
from usvideos group by title) a )a where rnk<=3;

# ●	Top 3 channels By number of total views 

# Wrong
select * from(
select a.*, rank() over (order by total_views desc) rnk from(
select channel_title, sum(views) total_views 
from usvideos group by channel_title) a )a where rnk<=3;

#correct
select * from(
select a.*, rank() over (order by total_views desc) rnk from(
select channel_title, sum(views) total_views from(
select video_id, title, channel_title, max(views) views from usvideos group by title ) a group by channel_title) a )a where rnk<=3;

# ●	Top 3 channels By Likes or dislikes ratio is highest

#wrong
select * from(
select a.*, rank() over (order by ratio desc) rnk from(
select channel_title, case when dislikes = 0 then sum(likes) else sum(likes)/sum(dislikes) end ratio 
from usvideos group by channel_title) a )a where rnk<=3;

#correct
select * from(
select a.*, rank() over (order by ratio desc) rnk from(
select channel_title, sum(likes), sum(dislikes), case when sum(dislikes) = 0 then sum(likes) else sum(likes)/sum(dislikes) end ratio from (
select video_id, title, channel_title, max(likes) likes,  max(dislikes)  dislikes from usvideos group by title 
) a group by channel_title ) a )a where rnk<=3;

# ●	Top 3 channels By number of total comments

#wrong
select * from(
select a.*, rank() over (order by total_comments desc) rnk from(
select channel_title, sum(comment_count) total_comments 
from usvideos group by channel_title) a )a where rnk<=3;

#correct
select * from(
select a.*, rank() over (order by total_comments desc) rnk from(
select channel_title, sum(comment_count) total_comments from(
select video_id, title, channel_title, max(comment_count) comment_count from usvideos group by title 
)a group by channel_title) a )a where rnk<=3;


#	Top 3 categories By number of total views 

select * from(
select c.*, rank() over (order by total_views desc) rnk from(
select category_id, category_name, sum(views) total_views from(
select category_id, category_name, max(views) views from(
select a.video_id, a.title, a.category_id, b.category_name, a.views from usvideos a 
left join  category_title b on a.category_id = b.category_id ) c group by title )c group by category_id, category_name ) c)c where rnk <=3;

#	Top 3 categories Likes or dislikes ratio is highest

#wrong
select * from(
select c.*, rank() over (order by ratio desc) rnk from(
select category_id, category_name, case when dislikes = 0 then sum(likes) else sum(likes)/sum(dislikes) end ratio from(
select a.category_id, b.category_name, a.likes, a.dislikes from usvideos a 
left join  category_title b on a.category_id = b.category_id ) c group by category_id, category_name ) c)c where rnk <=3;

#correct
select * from(
select c.*, rank() over (order by ratio desc) rnk from(
select category_id, category_name, case when dislikes = 0 then sum(likes) else sum(likes)/sum(dislikes) end ratio from(
select category_id, category_name, max(likes) likes, max(dislikes) dislikes from(
select a.video_id, a.title, a.category_id, b.category_name, a.likes, a.dislikes from usvideos a 
left join  category_title b on a.category_id = b.category_id ) c group by title )c group by category_id, category_name ) c)c where rnk <=3;

#	Top 3 categories By number of total comments

select * from(
select c.*, rank() over (order by total_comments desc) rnk from(
select category_id, category_name, sum(comment_count) total_comments  from(
select a.category_id, b.category_name, a.comment_count from usvideos a 
left join  category_title b on a.category_id = b.category_id ) c group by category_id, category_name ) c)c where rnk <=3;

select * from(
select c.*, rank() over (order by total_comments desc) rnk from(
select category_id, category_name, sum(comment_count) total_comments from(
select category_id, category_name, max(comment_count) comment_count from(
select a.video_id, a.title, a.category_id, b.category_name, a.comment_count from usvideos a 
left join  category_title b on a.category_id = b.category_id ) c group by title )c group by category_id, category_name ) c)c where rnk <=3;

# Number of videos published in each category.

select a.category_id, b.category_name, sum(distinct video_id) num_videos from usvideos a 
left join  category_title b on a.category_id = b.category_id group by a.category_id, b.category_name;


# Calculate any 3 videos which got at least 4 likes on every 100 views.

select * from(
select video_id, title, likes/views ratio from usvideos) a where ratio > (4/100)  limit 3;

# Calculate any 3 videos which got at least 5 comments on every 1000 views.

select * from(
select video_id, title, comment_count/views ratio from usvideos) a where ratio > (5/1000)  limit 3;



SELECT DATE_FORMAT(trending_date, "%Y %d %M ") from usvideos;

SELECT STR_TO_DATE(trending_date,'%Y %d,%M') from usvideos;

truncate table usvideos;

SELECT convert(trending_date, 101) from usvideos;

SELECT PARSE(trending_date AS date USING 'ANSI') AS Result;  

SELECT trending_date from usvideos;

select concat('20', substring(trending_date, 1, 2), '/', substring(trending_date, 7, 2), '/', substring(trending_date, 4, 2)) trend_date 
from usvideos; 

SELECT DATE(publish_time) from usvideos;

# Top 3 videos of each category in each year o	By number of views

select * from(
select c.*, rank() over (partition by category_id, tyear order by views desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, concat('20', substring(a.trending_date, 1, 2)) tyear, max(views) views from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

# Top 3 videos of each category in each year o	By number of comments 

select * from(
select c.*, rank() over (partition by category_id, tyear order by comments desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, concat('20', substring(a.trending_date, 1, 2)) tyear, max(comment_count) comments from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

# Top 3 videos of each category in each year o	By number of likes

select * from(
select c.*, rank() over (partition by category_id, tyear order by likes desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, concat('20', substring(a.trending_date, 1, 2)) tyear, max(likes) likes from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

# Top 3 videos of each category in each year o	Highest user interaction 

select * from(
select c.*, rank() over (partition by category_id, tyear order by user_interaction desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2)) tyear, max(views+likes+dislikes+comment_count) user_interaction from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

# ●	Top 3 videos in each month o	by views

select * from(
select c.*, rank() over (partition by ym order by views desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2), substring(a.trending_date, 7, 2)) ym, max(views) views from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

# ●	Top 3 videos in each month o	Likes or dislikes ratio is highest

select * from(
select c.*, rank() over (partition by ym order by ratio desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2), substring(a.trending_date, 7, 2)) ym, case when dislikes = 0 then likes else likes/dislikes end ratio from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

#●	Top 3 videos of each category in each month By number of views

select * from(
select c.*, rank() over (partition by category_id, ym order by views desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2), substring(a.trending_date, 7, 2)) ym, max(views) views from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

#Top 3 videos of each category in each month By number of likes

select * from(
select c.*, rank() over (partition by category_id, ym order by likes desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2), substring(a.trending_date, 7, 2)) ym, max(likes) likes from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;

#Top 3 videos of each category in each month By number of dislikes


select * from(
select c.*, rank() over (partition by category_id, ym order by dislikes desc) rnk from(
select a.video_id, a.title, a.category_id, b.category_name, 
concat('20', substring(a.trending_date, 1, 2), substring(a.trending_date, 7, 2)) ym, max(dislikes) dislikes from usvideos a 
left join  category_title b on a.category_id = b.category_id  group by title
) c)c where rnk <=3;


#●	Top 3 videos 1.	Value calculated by below formula is highest views on most recent date / (recent date – Publish date)

show variables like 'have_query_cache';



