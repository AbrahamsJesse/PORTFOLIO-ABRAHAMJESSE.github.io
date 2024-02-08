
Introduction:

This SQL file contains a series of queries designed to analyze the dataset of second-hand cars. The queries are 
organized into different sections, each addressing specific aspects of the analysis outlined in the README file. 
By employing various SQL functions and techniques, we aim to derive insights into pricing, market trends, performance,
and ownership analysis of the dataset.

The SQL queries are annotated to provide clarity on the purpose of each query and the analysis being performed. 
Additionally, comments are included to delineate different sections of the analysis and provide context for the queries.

Through this SQL analysis, I aim to provide valuable insights that can inform decision-making and strategic 
planning for buyers, sellers, and stakeholders in the used car market.


Sections of the analysis:
	- PRICING ANALYSIS 
	- MARKET TRENDS
	- PERFORMANCE AND SPECIFICATIONS
	- OWNERSHIP ANALYSIS


#Creation of the databse
create database cars;
use cars;
										#PRICING ANALYSIS :

/* AVERAGE SELLING PRICE OF CARDS DISTRIBUTED BY BRAND*/
	/*Sample from Table 1*/
	select  Car_name as Brand, ROUND(AVG(Selling_Price),2) as 'Average Price'
	from car_data
	group by Car_name
	order by 'Average Price' DESC;
    
	/*Sample from Table 4*/
	select  Make as Brand, ROUND(AVG(Price),0) as 'Average Price'
	from car_data_4
	group by Brand
	order by 'Average Price' DESC;

/*COMPARISON OF THE AVERAGE ORIGINAL PRICE AND THESELLING PRICE OF CARS IN TABLE 1 OF THE DATASET*/
	WITH CTE_AVG as(
		select  ROUND(AVG(Present_Price),2) as 'Average Original Price',
				ROUND(AVG(Selling_Price),2) as 'Average Selling Price',
				ROUND(AVG(Present_Price) - AVG(Selling_Price), 2) AS 'Average Price Difference'    
		from car_data)
	select *
	from CTE_AVG;
	/*Insight! - Once bought, the car loses 3 points of its price on average*/


/*VARIANCE OF THE SELLING PRICE BASED ON THE YEAR OF MANUFACTURE*/
	/*Sample form Table 1*/
	select Year, ROUND(AVG(Selling_price),2) as 'Average Selling Price', ROUND(AVG(Kms_Driven),0) as 'Kms Driven'
	from car_data
	group by Year
	order by Year;
	/*The newer the more expensive, and the newer the less kms driven*/
    
	/*Sample form Table 4*/
    select Year, ROUND(AVG(Price),0) as 'Average Selling Price', ROUND(AVG(Kilometer),0) as 'Kms Driven'
	from car_data_4
	group by Year
	order by Year;
	/*The newer the more expensive, and the newer the less kms driven. Insight! - There are variances and exceptions*/


							#MARKET TRENDS
/* MOST USUAL SELLER OF SECOND HAND CARS*/
	select Seller_type as 'Seller Type', count(Seller_type) as 'Count'
	from car_data
	group by Seller_type;
	/*Dealers are the most common seller type*/

/*LEAST LIKELY CARS TO BE SOLD*/
	select Car_Name as 'Car Brand', Year, ROUND(AVG(Kms_Driven),0) as 'Average Kms'
	from car_data
	group by Car_Name, Year
	order by AVG(Kms_Driven) DESC
	Limit 5;
	/*The lest likely models to be sold are: Activa 3g, camry, corolla, Honda Karizma and fortuner;*/

								#PERFORMANCE AND SPECIFICATIONS:
/*JOINS*/
/*LETS UNIFY THE DATA FROM TABLE 1 and 2 TO CHECK THE Kms DRIVEN TO COMPARE IT SIDE BY SIDE*/
	select car_data.Car_Name as 'Brand Car - Table 1', car_data.Year, ROUND(AVG(car_data.Kms_Driven),0) as 'Kms',
			car_data_2.name as 'Brand Car - Table 2', car_data_2.Year as 'Year', ROUND(AVG(car_data_2.km_driven),0) as 'Kms'
	from car_data
	inner join(
		select*
		from car_data_2) as car_data_2
	on car_data.Year= car_data_2.Year
	group by car_data.Car_Name, car_data.Year, car_data.Year, car_data_2.name;

							/*UNION */
/* LETS UNIFY THE DATA FROM TABLE 1 and 2 TO CHECK THE Kms DRIVEN UNIFYING THE ROWS*/
	select Brand, Year, Count(Brand) as 'Number of Units Available', ROUND(AVG(Kms),0) as 'Average Kms'
	from(
		select car_data.Car_Name as Brand, car_data.Year as Year, car_data.Kms_Driven as Kms
		from car_data
		union all
		select car_data_2.name as Brand, car_data_2.Year as Year, car_data_2.km_driven as Kms
		from car_data_2) as Table_combined
	group by Year, Brand;

/*MOST COMMON FUEL TYPES AMONG THE LISTED CARDS IN ALL TABLES*/
	SELECT Fuel_Type as 'Fuel Type', COUNT(*) AS Ocurrences
	from(
		select car_data.Fuel_Type
		from car_data
		union all
		select car_data_2.fuel as Fuel_Type
		from car_data_2
		union all
		select car_data_3.fuel as Fuel_Type
		from car_data_3
		union all
		select car_data_4.`Fuel Type` AS Fuel_Type
		from car_data_4) as Tables_combined
	group by Fuel_type
	order by Ocurrences DESC;
	/*The most common Fuel type is Diesel closely followed by Petrol*/


/*TRENDS IN PRICING BASED ON THE FUEL TYPE */
	/*Table 1 (car_data)*/
	select Fuel_Type, ROUND(AVG(Selling_Price),0) as 'Average Price'
	from car_data
	group by Fuel_Type
	order by 'Average Price';

	/*Table 2 (car_data_2)*/
	select fuel, ROUND(AVG(Selling_Price),0) as 'Average Price'
	from car_data_2
	group by Fuel
	order by 'Average Price';

	/*Table 3 (car_data_3)*/
	select Fuel, ROUND(AVG(Selling_Price),0) as 'Average Price'
	from car_data_3
	group by Fuel
	order by 'Average Price';

	/*Table 4 (car_data_4)*/
	select `Fuel Type`, ROUND(AVG(Price),0) as 'Average Price'
	from car_data_4
	group by `Fuel Type`
	order by 'Average Price';
	/*Diesel is the most expensive, follow by Petrol, in all tables*/




/* HOW DOES SEATING CAPACITY CORRELATE WITH THE SELLING PRICE*/

	/*Lets check the most common units with seating capacity*/
    select price, `Seating Capacity`
    from car_data_4;
    SELECT `Seating Capacity`, COUNT(*) AS Count
	FROM car_data_4
	GROUP BY `Seating Capacity`
	ORDER BY Count DESC
	LIMIT 4;
    /* The most oferred car are the ones with seating capacity of 5 units*/
    
    SELECT `Seating Capacity`, round(AVG(Price),0) AS Avg_Price
	FROM car_data_4
	GROUP BY `Seating Capacity`
	ORDER BY Avg_Price DESC
	LIMIT 3;
	/* However, the most expensive as average are those with 2 and 6 seating capacity*/


    
	


/*LETS TAKE A QUICK VIEW OF THE SEATING CAPACITY AND THE PRICES*/
	select price, `Seating Capacity`
	from car_data_4
    ;
	select`Seating Capacity`, count(`Seating Capacity`)
	from car_data_4
    where `Seating Capacity` = 5
    ;
    select`Seating Capacity`, count(`Seating Capacity`)
	from car_data_4
    where `Seating Capacity` = 2
    ;
	
/*Quick overview: Cars with 2 and 5 seating capacity seem to be the most expensive as a general rule*/
	select Price, COUNT(`Seating Capacity`) as 'Seating Capacity'
	from car_data_4
	where `Seating Capacity` = 2
	group by Price
	order by Price DESC;

	select Price, COUNT(`Seating Capacity`) as 'Seating Capacity'
	from car_data_4
	where `Seating Capacity` = 5
	group by Price
	order by Price DESC;
	/*There is a slight correlation. When sorting the Seating Capacity by Price we see that the majority of the 
	highest prices have 1 seats.*/





	/*SHOWCASE OF BASIC SKILLS - LIKE,AS,IN,BETWEEN,TOP,GROUP BY, limit, ORDERY, HAVING, EXISTS, AND, ASC/DESC*/
	select name as Brand , max(selling_price) as 'Maximum Selling Price'
	from car_data_3
	group by name
	order by name ASC;

	select *
	from car_data_3
	where selling_price like 10000000;

	select name as Brand, year as Year, selling_price as 'Price', owner as 'Owner', fuel as 'Type of Fuel'
	from car_data_3
	where year between 2017 and 2018 and owner like 'First Owner' and fuel like 'Diesel' and selling_price >20500
	order by price DESC
	limit 10;

                /* VIEWs and CTEs*/
/*Creation of a View for the Brand Toyota in order to filter 
only the information for this brand*/

	CREATE VIEW Car_data_4_Toyota_view as
		select *
		from car_data_4
        where Make like 'Toyota';
        
		select *
		from Car_data_4_Toyota_view
		where model like 'Glanza G';
		/* In this way we filter for a specific model*/


		select Make as Brand, model, Price
		from Car_data_4_Toyota_view
		where model like '%Glanza%';

/*Creation of a View for the Brand BMW in order to filter 
only the information for this brand*/
	CREATE VIEW Car_data_4_BMW_view as
			select Make, Model, Year, Price, Color, Location, Owner
			from car_data_4
			where Make like 'BMW';
	select *
	from Car_data_4_BMW_view;

/*Creation of a CTE for the Brand Toyota in order to filter with 
the information for this brand */

	WITH CTE_Toyota as (
		select *
		from car_data_4
		where Make like 'Toyota')
		
	select Make, Model, Price, Year, Location
	from CTE_Toyota
	where Model like '%Glanza%' and Year like 2019 and Price > 750000;


/*Creation of a CTE for the Brand BWM in order to filter with 
the information for this brand */
	WITH CTE_BMW as (
		select *
		from car_data_4
		where Make like 'BMW')
		
	select Make, Model, Price 
	from CTE_BMW
	where Model like '%Series%'
	group by Make, Model, Price;

						#OWNERSHIP ANALYSIS 
/*TRENDS IN PRICING BASED ON THE SELLER TYPE*/
	/*From Table 1(car_data)*/
	SELECT Seller_Type, Year, ROUND(AVG(Selling_Price), 0) AS 'Average Price'
	FROM car_data
	WHERE Year IN ( #this subquery is to show only years and price that are present in the three of the seller type
		SELECT Year
		FROM car_data
		GROUP BY Year
		HAVING COUNT(DISTINCT Seller_Type) = (SELECT COUNT(DISTINCT Seller_Type) FROM car_data)
	)
	GROUP BY Seller_Type, Year
	ORDER BY Year;
/*We can observe a trend: Dealer type of seller presents a more expensive offer*/

	/*From Table 2 (car_data_2)*/
	SELECT Seller_Type, Year, ROUND(AVG(Selling_Price), 0) AS 'Average Price'
	FROM car_data_2
	WHERE Year IN ( #this subquery is to show only years and price that are present in the three of the seller type
		SELECT Year
		FROM car_data_2
		GROUP BY Year
		HAVING COUNT(DISTINCT Seller_Type) = (SELECT COUNT(DISTINCT Seller_Type) FROM car_data_2)
	)
	GROUP BY Seller_Type, Year
	ORDER BY Year;
	/*We can observe a trend: Dealer type of seller presents a more expensive offer, closely follow by
	Trustmark Dealer in some cases*/

	/*From Table 3 (car_data_3)*/
	SELECT Seller_Type, Year, ROUND(AVG(Selling_Price), 0) AS 'Average Price'
	FROM car_data_3
	WHERE Year IN ( #this subquery is to show only years and price that are present in the three of the seller type
		SELECT Year
		FROM car_data_3
		GROUP BY Year
		HAVING COUNT(DISTINCT Seller_Type) = (SELECT COUNT(DISTINCT Seller_Type) FROM car_data_3)
	)
	GROUP BY Seller_Type, Year
	ORDER BY Year;
	/*We can observe very inconsistent data. However, then again Dealer type of seller presents a more expensive offer*/
	/*Table 4 (car_data_4)*/
	SELECT `Seller Type`, Year, ROUND(AVG(Price), 0) AS 'Average Price'
	FROM car_data_4
	WHERE Year IN ( #this subquery is to show only years and price that are present in the three of the seller type
		SELECT Year
		FROM car_data_4
		GROUP BY Year
		HAVING COUNT(DISTINCT `Seller Type`) = (SELECT COUNT(DISTINCT `Seller Type`) FROM car_data_4)
	)
	GROUP BY `Seller Type`, Year
	ORDER BY Year;
	/*We can observe a trend: Corporate type of seller presents a more expensive offer*/




indexes:
Demonstrates your understanding of optimizing query performance by creating appropriate indexes on columns.










Pricing Analysis:

Market Trends:
Is there a correlation between the age of a car (year) and its selling price?
How does the distribution of cars differ across locations?

Performance and Specifications:
What is the average mileage of the cars?
How does seating capacity correlate with the selling price?
Ownership Analysis:

How does the ownership pattern vary across different car models?
Inventory Insights:
What is the distribution of cars based on their make and model?
How does the distribution of cars vary based on fuel type and transmission?
Seller Type Analysis:
What is the average selling price for cars sold by different seller types?
Are there particular seller types associated with higher-priced cars?
Transmission Preferences:

What is the distribution of cars based on the number of owners?
Are there any patterns in selling prices based on the number of owners?
What is the distribution of cars based on transmission type (automatic or manual)?
Are there particular seller types associated with higher-priced cars?
Do automatic transmission cars have a different selling price distribution compared to manual transmission cars?
Are there specific locations where certain types of cars are more prevalent?

Dimension Analysis:
How do the dimensions (length, width, height) of cars vary across different models?
Is there any correlation between dimensions and selling price?
Fuel Efficiency Comparison:
How does fuel efficiency (mileage) vary across different fuel types?
Is there a relationship between fuel efficiency and selling price?

____;



What is the distribution of cars based on the number of owners?
Are there any patterns in selling prices based on the number of owners?
What is the distribution of cars based on transmission type (automatic or manual)?
Are there particular seller types associated with higher-priced cars?
Do automatic transmission cars have a different selling price distribution compared to manual transmission cars?
Are there specific locations where certain types of cars are more prevalent?


Integration with External Systems:
If your SQL project interacts with other systems, demonstrate this integration and data flow.

indexes:
Demonstrates your understanding of optimizing query performance by creating appropriate indexes on columns.

Constraints:
Illustrates the use of constraints (such as UNIQUE, CHECK, and DEFAULT constraints) to enforce data integrity.

Dynamic SQL:
Shows how to construct and execute SQL statements dynamically, allowing for more flexibility in query construction
