module Jekyll
  module CustomDateFormat
    def custom_date_format(input)
      return input unless input.is_a?(String)
      case input.length
      when 4
        Date.strptime(input, '%Y').strftime('%Y')
      when 7
        Date.strptime(input, '%Y-%m').strftime('%B %Y')
      when 10
        Date.strptime(input, '%Y-%m-%d').strftime('%B %d, %Y')
      else
        input
      end
    rescue ArgumentError
      input
    end
  end
end

Liquid::Template.register_filter(Jekyll::CustomDateFormat)
