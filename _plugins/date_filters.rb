require 'date'

module Jekyll
  module DateFilters
    def custom_date_format(date_str)
      begin
        case date_str.count('-')
        when 2
          date = Date.strptime(date_str, '%Y-%m-%d')
          date.strftime('%B %d, %Y')  # e.g., January 01, 2023
        when 1
          date = Date.strptime(date_str, '%Y-%m')
          date.strftime('%B %Y')      # e.g., March 2018
        else
          date = Date.strptime(date_str, '%Y')
          date.strftime('%Y')         # e.g., 2023
        end
      rescue
        date_str  # Return the original string if parsing fails
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::DateFilters)
