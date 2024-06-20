require 'date'

module Jekyll
  module DateFilters
    def custom_date_format(date_str)
      begin
        date = Date.parse(date_str)
        case date_str.count('-')
        when 2
          date.strftime('%B %d, %Y')  # YYYY-MM-DD format
        when 1
          date.strftime('%B %Y')      # YYYY-MM format
        else
          date.strftime('%Y')         # YYYY format
        end
      rescue
        date_str  # Return original string if parsing fails
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::DateFilters)
